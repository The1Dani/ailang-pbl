import pandas as pd

from ailang.engine.AiLangFunc import makeMethod
from ailang.engine.AiLangObj import AiLangObj, fromDFtoObj
from ailang.engine.AiLangType import DfType


@makeMethod("dropna_ip", DfType, [])
def dfBuiltinDropnaInplace(parent, *items):
    if not isinstance(parent, AiLangObj):
        raise ValueError()
    df = parent.get().get()
    if not isinstance(df, pd.DataFrame):
        raise ValueError()

    df = df.dropna(*items)
    parent.update(fromDFtoObj(parent.ident, df))

    return parent


@makeMethod("dropna", DfType, [])
def dfBuiltinDropna(parent, *items):
    if not isinstance(parent, AiLangObj):
        raise ValueError()
    df = parent.get().get()
    if not isinstance(df, pd.DataFrame):
        raise ValueError()

    df = df.dropna(*items)

    return fromDFtoObj(parent.ident, df)
