from typing import Callable
from AiLangObj import AiLangObj, NoneObj
from AiLangType import AiLangType
from grammar.AiLangParser import AiLangParser as ap
from utils import getTerminalSymbol, Singleton
import utils


class AiLangFunc:
    def __init__(self, id: str, func: Callable[..., AiLangObj], args: list[str]):
        self.id: str = id
        self.func: Callable[..., AiLangObj] = func
        self.args: list[str] = args

    def call(self, args: list[AiLangObj]) -> AiLangObj:
        return self.func(*args)

    @staticmethod
    def make(
        node: ap.Func_defContext,
        ctxRunnerConstructor: Callable[
            [ap.ContextContext], Callable[..., dict[int, AiLangObj]]
        ],
    ) -> AiLangFunc:
        ids = utils.getAllIds(node)
        ctx = node.getTypedRuleContext(ap.ContextContext, 0)
        if ctx is None:
            raise ValueError()
        funcID = ids.pop(0)
        func = AiLangFunc.constructCallableFromCtx(ctxRunnerConstructor(ctx))
        return AiLangFunc(funcID, func, ids)

    @staticmethod
    def constructCallableFromCtx(
        ctxRunner: Callable[..., dict[int, AiLangObj]],
    ) -> Callable[..., AiLangObj]:
        def wrapper(*args) -> AiLangObj:
            vars = ctxRunner(*args)
            if -1 not in vars:
                return NoneObj()
            return vars[-1]

        return wrapper


class Space(metaclass=Singleton):
    def __init__(self) -> None:
        pass


class FunctionSpace(Space):

    def __init__(self):
        super().__init__()
        self.functions: dict[str, AiLangFunc] = {}

    def addFunc(self, func: AiLangFunc) -> None:
        if func.id in self.functions:
            raise ValueError("The function already exists")
        self.functions[func.id] = func

    def hasFunc(self, id: str) -> bool:
        if id in self.functions:
            return True
        return False

    def call(self, id: str, args) -> AiLangObj:
        if id in self.functions:
            func = self.functions[id]
            return func.call(args)
        raise ValueError("The function is not available")


class MethodSpace(Space):
    def __init__(self):
        super().__init__()
        self.functions: dict[str, dict[str, AiLangFunc]] = {}

    def addFunc(self, ttype: type, func: AiLangFunc) -> None:
        if str(ttype) not in self.functions:
            self.functions[str(ttype)] = {}
        if func.id in self.functions[str(ttype)]:
            raise ValueError("The method already exists")
        self.functions[str(ttype)][func.id] = func

    def hasMethod(self, ttype: type, id: str) -> bool:
        print(str(ttype))
        if str(ttype) in self.functions:
            if id in self.functions[str(ttype)]:
                return True
        return False

    def call(self, parent: AiLangObj, id: str, args) -> AiLangObj:
        """As a convention the first arg of every method is the parent object"""
        ttype = type(parent.val)
        if str(ttype) in self.functions:
            if id in self.functions[str(ttype)]:
                func = self.functions[str(ttype)][id]
                args.append(parent)
                return func.call(args)
            raise ValueError(f"type {str(ttype)} does not have method {id}")
        raise ValueError(f"Type {ttype} does not have methods")


def makeFunc(funcId: str, argNames: list[str] = []):

    def wrapper(func: Callable[..., AiLangObj]):
        aFunc = AiLangFunc(
            id=funcId,
            func=func,
            args=argNames,
        )
        FunctionSpace().addFunc(aFunc)

        return func

    return wrapper


def makeMethod(methodId: str, ttype: type, argNames: list[str] = []):

    def wrapper(func: Callable[..., AiLangObj]):
        aMethod = AiLangFunc(id=methodId, func=func, args=argNames)

        MethodSpace().addFunc(ttype=ttype, func=aMethod)

        return func

    return wrapper
