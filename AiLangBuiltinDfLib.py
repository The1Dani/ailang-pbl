from AiLangFunc import makeMethod
from AiLangObj import AiLangObj, fromDFtoObj
from AiLangType import DfType
import pandas as pd


@makeMethod("dropna_ip", DfType, [])
def DfBuiltinDropnaInplace(parent, *items):
    if not isinstance(parent, AiLangObj):
        raise ValueError()
    df = parent.get()
    if not isinstance(df, pd.DataFrame):
        raise ValueError()

    df.dropna(*items)
    parent.update(fromDFtoObj(parent.id, df))

    return parent


@makeMethod("dropna", DfType, [])
def DfBuiltinDropna(parent, *items):
    if not isinstance(parent, AiLangObj):
        raise ValueError()
    df = parent.get()
    if not isinstance(df, pd.DataFrame):
        raise ValueError()

    df.dropna(*items)

    return fromDFtoObj(parent.id, df)
