"""Unicode surrogate sanitizer.

Removes unpaired Unicode surrogates that cause JSON serialization errors.
Valid emoji and other supplementary characters (properly paired surrogates) are preserved.
"""

from __future__ import annotations

import re

# Match unpaired surrogates:
# - High surrogate (U+D800-U+DBFF) not followed by low surrogate
# - Low surrogate (U+DC00-U+DFFF) not preceded by high surrogate
# In Python 3, strings are sequences of Unicode code points, so lone surrogates
# only appear in data decoded with errors='surrogatepass' or constructed manually.
_LONE_SURROGATE = re.compile(
    r"[\ud800-\udbff](?![\udc00-\udfff])"  # high not followed by low
    r"|"
    r"(?<![\ud800-\udbff])[\udc00-\udfff]",  # low not preceded by high
)


def sanitize_surrogates(text: str) -> str:
    """Remove unpaired Unicode surrogate characters from *text*.

    Properly paired surrogates (emoji, CJK extension B, etc.) are preserved.

    >>> sanitize_surrogates("Hello 🙈 World")
    'Hello 🙈 World'
    """
    return _LONE_SURROGATE.sub("", text)
