import sys
import codecs
from AiLangFunc import makeFunc, makeMethod
from AiLangObj import AiLangObj, NoneObj
import AiLangBuiltinDfLib as _
from FuncUtils import getVars


def toStringDecoded(obj: AiLangObj) -> str:
    val = obj.get().get()
    return codecs.decode(str(val), "unicode-escape")


@makeFunc("print", ignore_arg_count=True)
def aiLangBuiltinPrint(*args, **kwargs) -> AiLangObj:

    args = list(args)

    sep, end = None, None

    if "sep" in kwargs:
        sep = toStringDecoded(kwargs["sep"])
        del kwargs["sep"]

    if "end" in kwargs:
        end = toStringDecoded(kwargs["end"])
        del kwargs["end"]

    kwarg_vals = list(kwargs.values())
    args += kwarg_vals

    print(f"DEBUG: {args}")

    values = [toStringDecoded(val) for val in args]

    print(*values, sep=sep, end=end)

    return NoneObj()


@makeFunc("exit", [], kwargs={"ret_code": NoneObj()})
def aiLangBuiltinExit(*args, **kwargs):

    vs = getVars(args, kwargs)
    ret_code = vs["ret_code"] if isinstance(vs["ret_code"], int) else 0

    ret_code = ret_code if ret_code else 0
    sys.exit(ret_code)


@makeMethod("rest", type(None))
def aiLangBuiltinDFRest(
    parent, *args, **kwargs
) -> AiLangObj:  # pylint: disable=unused-argument
    print(f"[DEBUG] {parent=} {args=} {kwargs=}")
    return AiLangObj("")


@makeFunc("breakpoint")
def aiLangInternalBreakPoint() -> AiLangObj:
    breakpoint()  # pylint: disable=forgotten-debug-statement
    return NoneObj()
