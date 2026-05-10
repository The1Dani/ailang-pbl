from __future__ import annotations
from types import UnionType
from typing import Callable, NoReturn, Protocol, Union
import copy

from AiLangObj import AiLangObj, NoneObj
from utils import Singleton


# Python typing black magic for function types
class AiLangCallable0(Protocol):
    """AiLang Callable definition with no arguments"""

    def __call__(self) -> AiLangObj: ...
class AiLangCallable1(Protocol):
    """AiLang Callable definition with positional arguments"""

    def __call__(self, *args: AiLangObj) -> AiLangObj: ...
class AiLangCallable2(Protocol):
    """AiLang Callable definition with positional arguments and keyword arguments"""

    def __call__(self, *args: AiLangObj, **kwargs: AiLangObj) -> AiLangObj: ...


AiLangCallable = Union[AiLangCallable0, AiLangCallable1, AiLangCallable2]


class AiLangFunc:
    """
    The function class for AiLang
    """

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments
        self,
        ident: str,
        func: AiLangCallable,
        args: list[str],
        kwargs: dict[str, AiLangObj],
        ignore_arg_count: bool = False,
    ):
        self.ident: str = ident
        self.func: AiLangCallable = func
        self.args: list[str] = args
        self.kwargs: dict[str, AiLangObj] = kwargs
        self.ignore_arg_count: bool = ignore_arg_count

    def call(self, args: list[AiLangObj], kwargs: dict[str, AiLangObj]) -> AiLangObj:
        local_kwargs = copy.deepcopy(self.kwargs)
        local_kwargs = {} if local_kwargs is None else local_kwargs

        special_args = list(
            filter(
                lambda arg: (
                    len(arg.ident) > 2 and arg.ident[0] == "_" and arg.ident[-1] == "_"
                ),
                args,
            )
        )

        # Tag arguments with their arg_names
        # Note that we are modifing the original args list implicitly
        filtered_args = list(filter(lambda arg: arg not in special_args, args))
        if len(self.args) == len(filtered_args):
            for arg, arg_name in zip(filtered_args, self.args):
                arg.ident = arg_name

        for key, val in kwargs.items():
            local_kwargs[key] = val

        # Tag kwargs with their dict_keys
        for k, v in local_kwargs.items():
            v.ident = k

        return self.func(*args, **local_kwargs)

    @staticmethod
    def constructCallableFromCtx(
        ctx_runner: Callable[[AiLangCallable], dict[int, AiLangObj]],
    ) -> AiLangCallable:
        def wrapper(*args, **kwargs) -> AiLangObj:
            variables = ctx_runner(*args, **kwargs)
            if -1 not in variables:
                return NoneObj()
            return variables[-1]

        return wrapper

    def isValidCall(self, args: list[AiLangObj], kwargs: dict[str, AiLangObj]) -> bool:
        """This methods returns True if the args and kwargs are
        correctly passed in the point of view of the count."""

        if self.ignore_arg_count:
            return True

        expected_arg_count = len(self.args)
        kwargs = self.kwargs
        kwarg_count = len(kwargs)

        if (
            len(args) < expected_arg_count
            or len(args) > expected_arg_count + kwarg_count
        ):
            return False

        expected_kwarg_names = set(self.kwargs.keys())
        kwarg_names = set(kwargs.keys())

        if not kwarg_names.issubset(expected_kwarg_names):
            return False

        return True

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
            if not func.isValidCall(args, kwargs):
                raise ValueError("Invalid Passed arguments")
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
                parent.old_ident = parent.ident
                parent.ident = "_parent_"
                args.insert(0, parent)
                return func.call(args, kwargs)
            raise ValueError(f"type {str(ttype)} does not have method {ident}")
        raise ValueError(f"Type {ttype} does not have methods")


def makeFunc(
    func_id: str,
    arg_names: list[str] | None = None,
    kwargs: dict[str, AiLangObj] | None = None,
    ignore_arg_count: bool = False,
) -> Callable[[AiLangCallable], AiLangCallable] | NoReturn:

    arg_names = [] if arg_names is None else arg_names
    kwargs = (
        {}
        if kwargs is None
        else {
            ident: (setattr(obj, "ident", ident) if obj is not NoneObj() else None)
            or obj
            for ident, obj in kwargs.items()
        }
    )

    def wrapper(func: AiLangCallable):
        fn = AiLangFunc(
            ident=func_id,
            func=func,
            args=arg_names,
            kwargs=kwargs,
            ignore_arg_count=ignore_arg_count,
        )
        FunctionSpace().addFunc(fn)

        return func

    return wrapper


def makeMethod(
    method_id: str,
    ttype: type | UnionType,
    arg_names: list[str] | None = None,
    kwargs: dict[str, AiLangObj] | None = None,
    ignore_arg_count: bool = False,
):
    """As a convention the first arg of every method is the parent object"""

    arg_names = [] if arg_names is None else arg_names
    kwargs = {} if kwargs is None else kwargs

    types_to_add = []

    if isinstance(ttype, type):
        types_to_add.append(ttype)
    if isinstance(ttype, UnionType):
        types_to_add += list(ttype.__args__)

    def wrapper(func: AiLangCallable):
        method = AiLangFunc(
            ident=method_id,
            func=func,
            args=arg_names,
            kwargs=kwargs,
            ignore_arg_count=ignore_arg_count,
        )

        for _type in types_to_add:
            MethodSpace().addFunc(ttype=_type, func=method)

        return func

    return wrapper
