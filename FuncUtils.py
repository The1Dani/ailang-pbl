from typing import Any, Optional, Union, overload
from AiLangObj import AiLangObj, NoneObj
import AiLangType


@overload
def getVars(args: tuple[AiLangObj], kwargs: dict[str, AiLangObj]) -> dict[str, Any]:
    """Get the named arguments as unwrapped in a dict"""


@overload
def getVars(args: dict[str, AiLangObj]) -> dict[str, Any]:
    """Get the named arguments as unwrapped in a dict"""


@overload
def getVars(args: tuple[AiLangObj]) -> dict[str, Any]:
    """Get the named arguments as unwrapped in a dict"""


def unwrap(args: list) -> dict[str, Any]:
    variables = {}
    for arg in args:
        variables[arg.ident] = arg.get().get() if arg is not NoneObj() else None
    return variables


def unwrapValue(value: AiLangObj | AiLangType.AiLangType | Any) -> Any:
    """Unwrap AiLang objects to underlying Python values.

    Handles AiLangObj, AiLangType, and returns the raw Python value.
    """
    if isinstance(value, AiLangObj):
        value = value.get()
    if hasattr(value, "get"):
        value = value.get()
    return value


def getVars(
    args: Union[tuple[AiLangObj], dict[str, AiLangObj]],
    kwargs: Optional[dict[str, AiLangObj]] = None,
) -> dict[str, Any]:

    if isinstance(args, dict):
        return unwrap(list(args.values()))

    if isinstance(args, tuple) and kwargs is None:
        return unwrap(list(filter(lambda arg: arg.ident != "", args)))

    if kwargs is not None:
        to_unwrap = list(filter(lambda arg: arg.ident != "", args)) + list(
            kwargs.values()
        )
        return unwrap(to_unwrap)

    raise ValueError("Unreachable")
