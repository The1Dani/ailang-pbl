from __future__ import annotations
from typing import Callable
from AiLangObj import AiLangObj, NoneObj
from utils import Singleton


class AiLangFunc:
    """
    The function class for AiLang
    """

    def __init__(
        self,
        ident: str,
        func: Callable[..., AiLangObj],
        args: list[str],
        kwargs: dict[str:AiLangObj],
    ):
        self.ident: str = ident
        self.func: Callable[..., AiLangObj] = func
        self.args: list[str] = args
        self.kwargs: dict[str:AiLangObj] = kwargs

    def call(self, args: list[AiLangObj]) -> AiLangObj:
        return self.func(*args)

    @staticmethod
    def constructCallableFromCtx(
        ctx_runner: Callable[..., dict[int, AiLangObj]],
    ) -> Callable[..., AiLangObj]:
        def wrapper(*args) -> AiLangObj:
            variables = ctx_runner(*args)
            if -1 not in variables:
                return NoneObj()
            return variables[-1]

        return wrapper

    def __repr__(self) -> str:
        args = ", ".join(self.args)
        return f"{self.ident}({args})"


class Space(metaclass=Singleton):
    """Abstract Class for Spaces that needs to be Singletons"""

    def __init__(self) -> None:
        pass


class FunctionSpace(Space):
    """Function Space that stores the available functions, Its a singleton class"""

    def __init__(self):
        super().__init__()
        self.functions: dict[str, AiLangFunc] = {}

    def addFunc(self, func: AiLangFunc) -> None:
        if func.ident in self.functions:
            raise ValueError("The function already exists")
        self.functions[func.ident] = func

    def hasFunc(self, ident: str) -> bool:
        if ident in self.functions:
            return True
        return False

    def call(
        self, ident: str, args: list[AiLangObj], kwargs: dict[str, AiLangObj]
    ) -> AiLangObj:
        if ident in self.functions:
            func = self.functions[ident]
            return func.call(args, kwargs)
        raise ValueError("The function is not available")


class MethodSpace(Space):
    """Method Space that stores the available methods, Its a singleton class"""

    def __init__(self):
        super().__init__()
        self.functions: dict[str, dict[str, AiLangFunc]] = {}

    def addFunc(self, ttype: type, func: AiLangFunc) -> None:
        if str(ttype) not in self.functions:
            self.functions[str(ttype)] = {}
        if func.ident in self.functions[str(ttype)]:
            raise ValueError("The method already exists")
        self.functions[str(ttype)][func.ident] = func

    def hasMethod(self, ttype: type, ident: str) -> bool:
        # print(str(ttype))
        if str(ttype) in self.functions:
            if ident in self.functions[str(ttype)]:
                return True
        return False

    def call(
        self,
        parent: AiLangObj,
        ident: str,
        args: list[AiLangObj],
        kwargs: dict[str, AiLangObj],
    ) -> AiLangObj:
        """As a convention the first arg of every method is the parent object"""
        ttype = type(parent.val)
        if str(ttype) in self.functions:
            if ident in self.functions[str(ttype)]:
                func = self.functions[str(ttype)][ident]
                args.append(parent)
                return func.call(args, kwargs)
            raise ValueError(f"type {str(ttype)} does not have method {ident}")
        raise ValueError(f"Type {ttype} does not have methods")


def makeFunc(
    func_id: str,
    arg_names: list[str] | None = None,
    kwargs: dict[str, AiLangObj] | None = None,
):

    arg_names = [] if arg_names is None else arg_names

    def wrapper(func: Callable[..., AiLangObj]):
        fn = AiLangFunc(ident=func_id, func=func, args=arg_names, kwargs=kwargs)
        FunctionSpace().addFunc(fn)

        return func

    return wrapper


def makeMethod(
    method_id: str,
    ttype: type,
    arg_names: list[str] | None = None,
    kwargs: dict[str, AiLangObj] | None = None,
):
    """As a convention the first arg of every method is the parent object"""

    arg_names = [] if arg_names is None else arg_names

    def wrapper(func: Callable[..., AiLangObj]):
        method = AiLangFunc(ident=method_id, func=func, args=arg_names, kwargs=kwargs)

        MethodSpace().addFunc(ttype=ttype, func=method)

        return func

    return wrapper
