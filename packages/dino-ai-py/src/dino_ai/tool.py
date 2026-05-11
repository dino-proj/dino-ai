"""@tool decorator — extract JSON Schema from function type hints.

Usage::

    @tool
    def get_weather(city: str, units: str = "celsius") -> str:
        \"\"\"Get the current weather for a city.\"\"\"
        ...

    # get_weather.as_tool() → Tool(name="get_weather", description="...", parameters={...})

Or with Annotated for richer schemas::

    from typing import Annotated

    @tool
    def search(
        query: Annotated[str, "The search query"],
        max_results: Annotated[int, "Maximum results to return"] = 10,
    ) -> str:
        \"\"\"Search the web.\"\"\"
        ...
"""

from __future__ import annotations

import inspect
from collections.abc import Callable
from typing import Any, get_args, get_origin, get_type_hints

from dino_ai.context import Tool

_PY_TYPE_TO_JSON: dict[type, str] = {
    str: "string",
    int: "integer",
    float: "number",
    bool: "boolean",
}


def _is_annotated(tp: Any) -> bool:
    """Check if a type is typing.Annotated."""
    origin = get_origin(tp)
    if origin is None:
        return False
    try:
        import typing
        return origin is getattr(typing, "Annotated", None)
    except AttributeError:
        return False


def _extract_annotated(tp: Any) -> tuple[Any, str | None]:
    """Extract the base type and optional description from Annotated[T, desc]."""
    if not _is_annotated(tp):
        return tp, None
    args = get_args(tp)
    base = args[0] if args else tp
    desc = None
    for arg in args[1:]:
        if isinstance(arg, str):
            desc = arg
            break
    return base, desc


def _type_to_json_schema(tp: Any) -> dict[str, Any]:
    """Convert a Python type hint to a JSON Schema fragment."""
    base, desc = _extract_annotated(tp)

    origin = get_origin(base)

    # list[T]
    if origin is list:
        item_args = get_args(base)
        schema: dict[str, Any] = {"type": "array"}
        if item_args:
            schema["items"] = _type_to_json_schema(item_args[0])
        if desc:
            schema["description"] = desc
        return schema

    # dict[str, T]
    if origin is dict:
        dict_args = get_args(base)
        schema = {"type": "object"}
        if len(dict_args) >= 2:
            schema["additionalProperties"] = _type_to_json_schema(dict_args[1])
        if desc:
            schema["description"] = desc
        return schema

    # Optional[T] = Union[T, None]
    import types
    if origin is types.UnionType or (origin is not None and str(origin).startswith("typing.Union")):
        union_args = get_args(base)
        non_none = [a for a in union_args if a is not type(None)]
        if len(non_none) == 1:
            schema = _type_to_json_schema(non_none[0])
            if desc:
                schema["description"] = desc
            return schema

    # Primitive types
    json_type = _PY_TYPE_TO_JSON.get(base)
    if json_type:
        schema = {"type": json_type}
        if desc:
            schema["description"] = desc
        return schema

    # Fallback
    schema = {"type": "string"}
    if desc:
        schema["description"] = desc
    return schema


def _function_to_tool(fn: Callable[..., Any]) -> Tool:
    """Extract a Tool definition from a decorated function."""
    name = fn.__name__
    description = inspect.getdoc(fn) or ""

    hints = get_type_hints(fn, include_extras=True)
    sig = inspect.signature(fn)

    properties: dict[str, Any] = {}
    required: list[str] = []

    for param_name, param in sig.parameters.items():
        if param_name in ("self", "cls"):
            continue
        if param_name == "return":
            continue

        tp = hints.get(param_name, str)
        prop_schema = _type_to_json_schema(tp)

        # Check if parameter has a default value
        if param.default is inspect.Parameter.empty:
            required.append(param_name)

        properties[param_name] = prop_schema

    parameters: dict[str, Any] = {
        "type": "object",
        "properties": properties,
    }
    if required:
        parameters["required"] = required

    return Tool(name=name, description=description, parameters=parameters)


class _ToolWrapper:
    """Wraps a function with `.as_tool()` access."""

    def __init__(self, fn: Callable[..., Any]) -> None:
        self._fn = fn
        self._tool: Tool | None = None
        self.__name__ = fn.__name__
        self.__doc__ = fn.__doc__
        self.__module__ = fn.__module__

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self._fn(*args, **kwargs)

    def as_tool(self) -> Tool:
        """Return the Tool definition extracted from type hints."""
        if self._tool is None:
            self._tool = _function_to_tool(self._fn)
        return self._tool


def tool(fn: Callable[..., Any]) -> _ToolWrapper:
    """Decorator that attaches a `.as_tool()` method to a function.

    The Tool's JSON Schema is derived from the function's type hints and docstring.
    """
    return _ToolWrapper(fn)
