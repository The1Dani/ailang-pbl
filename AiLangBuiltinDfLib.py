import pandas as pd

from AiLangFunc import makeMethod
from AiLangObj import AiLangObj, fromDFtoObj
from AiLangType import DfType


@makeMethod("dropna_ip", DfType, [])
def dfBuiltinDropnaInplace(parent, *items):
    if not isinstance(parent, AiLangObj):
        raise ValueError()
    df = parent.get()
    if not isinstance(df, pd.DataFrame):
        raise ValueError()

    df.dropna(*items)
    parent.update(fromDFtoObj(parent.ident, df))

    return parent


@makeMethod("dropna", DfType, [])
def dfBuiltinDropna(parent, *items):
    if not isinstance(parent, AiLangObj):
        raise ValueError()
    df = parent.get()
    if not isinstance(df, pd.DataFrame):
        raise ValueError()

    df.dropna(*items)

    return fromDFtoObj(parent.ident, df)
