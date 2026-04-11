from AiLangFunc import makeFunc, makeMethod
from AiLangObj import AiLangObj, NoneObj
from AiLangType import AiLangType, NumType, NumTypes


@makeFunc("print")
def AiLangBuiltinPrint(*items: AiLangObj | AiLangType) -> AiLangObj:

    for item in items:
        if isinstance(item, AiLangObj):
            item = item.get()

        val = item.get()
        print(val)

    return NoneObj()


@makeFunc("exit")
def AiLangBuiltinExit(*items):
    retCode = None
    if len(items) > 0:
        first = items[0]
        if isinstance(first.get(), NumType) and first.get().type == NumTypes.INT:
            retCode = first.get().get()

    retCode = retCode if retCode else 0
    exit(retCode)


@makeMethod("rest", type(None))
def AiLangBuiltinDFRest(parent, *args) -> AiLangObj:
    return AiLangObj("")
