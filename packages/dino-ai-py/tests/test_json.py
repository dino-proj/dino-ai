"""Tests for JSON repair and streaming parser."""

from __future__ import annotations

from dino_ai._json import parse_json_with_repair, parse_streaming_json, repair_json


def test_valid_json():
    assert parse_json_with_repair('{"key": "value"}') == {"key": "value"}


def test_repair_invalid_escape():
    raw = '{"path": "C:\\Users\\test"}'
    result = repair_json(raw)
    parsed = parse_json_with_repair(result)
    assert isinstance(parsed, dict)


def test_repair_control_chars():
    raw = '{"text": "line1\nline2"}'
    result = repair_json(raw)
    assert "\\n" in result


def test_streaming_empty():
    assert parse_streaming_json(None) == {}
    assert parse_streaming_json("") == {}
    assert parse_streaming_json("   ") == {}


def test_streaming_complete():
    result = parse_streaming_json('{"city": "Tokyo", "temp": 25}')
    assert result == {"city": "Tokyo", "temp": 25}


def test_streaming_partial_object():
    result = parse_streaming_json('{"city": "Tokyo", "temp": ')
    assert result.get("city") == "Tokyo"


def test_streaming_partial_string():
    result = parse_streaming_json('{"query": "hello wor')
    # Should at least parse the key
    assert isinstance(result, dict)
