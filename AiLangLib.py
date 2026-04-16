import sys
from AiLangFunc import makeFunc, makeMethod
from AiLangObj import AiLangObj, NoneObj
from AiLangType import AiLangType, NumType, NumTypes
import AiLangBuiltinDfLib as _


@makeFunc("print")
def aiLangBuiltinPrint(*items: AiLangObj | AiLangType) -> AiLangObj:

    for item in items:
        if isinstance(item, AiLangObj):
            item = item.get()

        val = item.get()
        print(val)

    return NoneObj()


@makeFunc("exit")
def aiLangBuiltinExit(*items):
    ret_code = None
    if len(items) > 0:
        first = items[0]
        if isinstance(first.get(), NumType) and first.get().type == NumTypes.INT:
            ret_code = first.get().get()

    ret_code = ret_code if ret_code else 0
    sys.exit(ret_code)


@makeMethod("rest", type(None))
def aiLangBuiltinDFRest(parent, *args) -> AiLangObj:  # pylint: disable=unused-argument
    return AiLangObj("")
