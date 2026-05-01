from typing import Any
from AiLangObj import AiLangObj, NoneObj


def getVars(args: tuple[AiLangObj], kwargs: dict[str, AiLangObj]) -> dict[str, Any]:
    """Get the named arguments as unwrapped in a dict"""
    variables = {}
    for arg in list(filter(lambda arg: arg.ident != "", args)) + list(kwargs.values()):
        variables[arg.ident] = arg.get().get() if arg is not NoneObj() else None
    return variables
