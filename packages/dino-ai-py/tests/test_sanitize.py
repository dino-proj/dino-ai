"""Tests for unicode surrogate sanitizer."""

from __future__ import annotations

from dino_ai._sanitize import sanitize_surrogates


def test_normal_text_unchanged():
    assert sanitize_surrogates("Hello, world!") == "Hello, world!"


def test_emoji_preserved():
    assert sanitize_surrogates("Hello 🙈 World") == "Hello 🙈 World"


def test_cjk_preserved():
    assert sanitize_surrogates("你好世界") == "你好世界"


def test_empty_string():
    assert sanitize_surrogates("") == ""
