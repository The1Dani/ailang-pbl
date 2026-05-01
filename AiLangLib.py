import sys
import codecs
from AiLangFunc import makeFunc, makeMethod
from AiLangObj import AiLangObj, NoneObj
from AiLangType import NumType, NumTypes
import AiLangBuiltinDfLib as _


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


@makeFunc("exit", kwargs={"ret_code": AiLangObj("ret_code", NumType(0, NumTypes.INT))})
def aiLangBuiltinExit(*_, **kwargs):
    ret_code = kwargs["ret_code"]
    first_type = ret_code.get()
    if isinstance(first_type, NumType):
        if first_type.type == NumTypes.INT:
            ret_code = first_type.get()

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
