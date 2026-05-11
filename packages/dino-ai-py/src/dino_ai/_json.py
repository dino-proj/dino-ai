"""Incremental JSON parser for streaming tool call arguments.

Handles:
- Complete JSON parsing with repair for malformed escapes
- Partial/incomplete JSON from streaming (best-effort)
"""

from __future__ import annotations

import json

_VALID_JSON_ESCAPES = frozenset('"\\bfnrtu/')

_CONTROL_CHAR_MAP = {
    "\b": "\\b",
    "\f": "\\f",
    "\n": "\\n",
    "\r": "\\r",
    "\t": "\\t",
}


def _escape_control_char(ch: str) -> str:
    if ch in _CONTROL_CHAR_MAP:
        return _CONTROL_CHAR_MAP[ch]
    return f"\\u{ord(ch):04x}"


def repair_json(raw: str) -> str:
    """Repair malformed JSON string literals.

    - Escapes raw control characters inside strings
    - Doubles backslashes before invalid escape sequences
    """
    result: list[str] = []
    in_string = False
    i = 0
    n = len(raw)

    while i < n:
        ch = raw[i]

        if not in_string:
            result.append(ch)
            if ch == '"':
                in_string = True
            i += 1
            continue

        if ch == '"':
            result.append(ch)
            in_string = False
            i += 1
            continue

        if ch == '\\':
            if i + 1 >= n:
                result.append('\\\\')
                i += 1
                continue

            next_ch = raw[i + 1]
            if next_ch == 'u':
                digits = raw[i + 2:i + 6]
                if len(digits) == 4 and all(c in '0123456789abcdefABCDEF' for c in digits):
                    result.append(f'\\u{digits}')
                    i += 6
                    continue

            if next_ch in _VALID_JSON_ESCAPES:
                result.append(f'\\{next_ch}')
                i += 2
                continue

            result.append('\\\\')
            i += 1
            continue

        # Control character inside string
        cp = ord(ch)
        if 0x00 <= cp <= 0x1F:
            result.append(_escape_control_char(ch))
        else:
            result.append(ch)
        i += 1

    return ''.join(result)


def parse_json_with_repair(raw: str) -> object:
    """Parse JSON, attempting repair if initial parse fails."""
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        repaired = repair_json(raw)
        if repaired != raw:
            return json.loads(repaired)
        raise


def _try_close_json(partial: str) -> str:
    """Attempt to close incomplete JSON by balancing brackets/braces."""
    s = partial.rstrip()

    # Strip trailing comma
    if s.endswith(','):
        s = s[:-1].rstrip()

    # Strip incomplete trailing value (e.g., `"key": ` or `"key": 12` without closing)
    # Try progressively removing trailing incomplete elements
    attempts = [s]

    # If ends with `: ` or `:`, strip key:value
    stripped = s.rstrip()
    if stripped.endswith(':'):
        # Remove the colon and the key before it
        before_colon = stripped[:-1].rstrip()
        if before_colon.endswith('"'):
            key_start = before_colon.rfind('"', 0, len(before_colon) - 1)
            if key_start >= 0:
                before_key = before_colon[:key_start].rstrip()
                if before_key.endswith(','):
                    before_key = before_key[:-1]
                attempts.append(before_key)

    # Remove incomplete string at the end (unmatched quote)
    quote_count = 0
    esc = False
    for ch in s:
        if esc:
            esc = False
            continue
        if ch == '\\':
            esc = True
            continue
        if ch == '"':
            quote_count += 1
    if quote_count % 2 == 1:
        last_quote = s.rfind('"')
        if last_quote >= 0:
            before = s[:last_quote].rstrip()
            if before.endswith(':'):
                before = before[:-1].rstrip()
                key_quote = before.rfind('"')
                if key_quote >= 0:
                    before_key = before[:key_quote].rstrip()
                    if before_key.endswith(','):
                        before_key = before_key[:-1]
                    attempts.append(before_key)
                else:
                    attempts.append(before)
            elif before.endswith(','):
                attempts.append(before[:-1])
            else:
                attempts.append(before)

    # Try each attempt, closing brackets
    for attempt in attempts:
        closed = _close_brackets(attempt)
        try:
            result = json.loads(closed)
            if isinstance(result, dict):
                return closed
        except (json.JSONDecodeError, ValueError):
            continue

    return _close_brackets(s)


def _close_brackets(s: str) -> str:
    """Close unmatched brackets/braces in a string."""
    stack: list[str] = []
    in_str = False
    escape = False
    for ch in s:
        if escape:
            escape = False
            continue
        if ch == '\\' and in_str:
            escape = True
            continue
        if ch == '"':
            in_str = not in_str
            continue
        if in_str:
            continue
        if ch in ('{', '['):
            stack.append('}' if ch == '{' else ']')
        elif ch in ('}', ']') and stack:
            stack.pop()

    return s + ''.join(reversed(stack))


def parse_streaming_json(partial: str | None) -> dict[str, object]:
    """Parse potentially incomplete JSON from streaming.

    Always returns a dict; never raises. Returns ``{}`` on failure.
    """
    if not partial or partial.strip() == '':
        return {}

    # Try complete parse first
    try:
        result = parse_json_with_repair(partial)
        if isinstance(result, dict):
            return result
        return {}
    except (json.JSONDecodeError, ValueError):
        pass

    # Try closing incomplete JSON
    try:
        closed = _try_close_json(partial)
        result = json.loads(closed)
        if isinstance(result, dict):
            return result
    except (json.JSONDecodeError, ValueError):
        pass

    try:
        closed = _try_close_json(repair_json(partial))
        result = json.loads(closed)
        if isinstance(result, dict):
            return result
    except (json.JSONDecodeError, ValueError):
        pass

    return {}
