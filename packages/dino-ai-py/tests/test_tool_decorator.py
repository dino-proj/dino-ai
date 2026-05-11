"""Tests for @tool decorator and JSON Schema extraction."""

from __future__ import annotations

from typing import Annotated

from dino_ai.tool import tool


@tool
def greet(name: str, greeting: str = "Hello") -> str:
    """Greet someone by name."""
    return f"{greeting}, {name}!"


@tool
def search(
    query: Annotated[str, "The search query"],
    max_results: Annotated[int, "Maximum number of results"] = 10,
) -> str:
    """Search the web for information."""
    return query


@tool
def no_params() -> str:
    """A tool with no parameters."""
    return "ok"


@tool
def complex_params(
    tags: list[str],
    metadata: dict[str, str],
    count: int,
    verbose: bool = False,
) -> str:
    """A tool with complex parameter types."""
    return "ok"


def test_basic_tool_schema():
    t = greet.as_tool()
    assert t.name == "greet"
    assert t.description == "Greet someone by name."
    assert t.parameters["type"] == "object"
    assert "name" in t.parameters["properties"]
    assert t.parameters["properties"]["name"]["type"] == "string"
    assert t.parameters["properties"]["greeting"]["type"] == "string"
    assert t.parameters["required"] == ["name"]


def test_annotated_descriptions():
    t = search.as_tool()
    assert t.name == "search"
    assert t.parameters["properties"]["query"]["description"] == "The search query"
    assert t.parameters["properties"]["max_results"]["description"] == "Maximum number of results"
    assert t.parameters["properties"]["max_results"]["type"] == "integer"
    assert t.parameters["required"] == ["query"]


def test_no_params_tool():
    t = no_params.as_tool()
    assert t.name == "no_params"
    assert t.parameters["properties"] == {}
    assert "required" not in t.parameters


def test_complex_types():
    t = complex_params.as_tool()
    props = t.parameters["properties"]
    assert props["tags"]["type"] == "array"
    assert props["tags"]["items"]["type"] == "string"
    assert props["metadata"]["type"] == "object"
    assert props["count"]["type"] == "integer"
    assert props["verbose"]["type"] == "boolean"
    assert set(t.parameters["required"]) == {"tags", "metadata", "count"}


def test_tool_is_callable():
    """Decorated function should still be callable."""
    result = greet("Alice")
    assert result == "Hello, Alice!"

    result2 = greet("Bob", greeting="Hi")
    assert result2 == "Hi, Bob!"


def test_tool_cached():
    """as_tool() should return the same Tool object on repeated calls."""
    t1 = greet.as_tool()
    t2 = greet.as_tool()
    assert t1 is t2
