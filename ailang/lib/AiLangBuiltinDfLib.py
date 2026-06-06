import pandas as pd
import numpy as np

from ailang.engine.AiLangFunc import makeMethod
from ailang.engine.AiLangObj import AiLangObj, fromDFtoObj, NoneObj
from ailang.engine.AiLangType import DfType
from .FuncUtils import getVars


def updateDfObj(parent_obj: AiLangObj, df: pd.DataFrame) -> AiLangObj:
    target = parent_obj.original_reference or parent_obj
    target.update(fromDFtoObj(target.ident, df))
    return target


@makeMethod("dropna_ip", DfType, [])
def dfBuiltinDropnaInplace(parent: AiLangObj, *items):
    df = parent.get().get()

    df = df.dropna(*items)
    parent.update(fromDFtoObj(parent.ident, df))
    return NoneObj()

@makeMethod("dropna", DfType, [])
def dfBuiltinDropna(parent, *items):
    df = parent.get().get()

    df = df.dropna(*items)

    return fromDFtoObj(parent.ident, df)


# vs["_parent_"]
@makeMethod("map_bool_cols", DfType, ["cols"])
def dfMapBoolCols(*args, **kwargs):
    vs = getVars(args, kwargs)
    df = vs["_parent_"]

    cols = vs.get("cols", []) # having cols in vs is guaranteed by the function signature
    cols = [str(col) for col in cols]

    mapping = {
        True: 1,
        False: 0,
        "True": 1,
        "False": 0,
        "true": 1,
        "false": 0,
    }

    df = df.copy()
    for col in cols:
        if col in df.columns:
            # Use replace instead of map to satisfy static typing (Pyright)
            # and to support dict-based value mapping across dtypes.
            ser = df[col].replace(mapping)
            # Ensure a consistent integer-like dtype when possible (handles bool/str cases).
            try:
                df[col] = ser.astype("Int64")
            except Exception:  # fallback if dtype conversion not applicable
                df[col] = ser

    return fromDFtoObj("", df)


@makeMethod("select_numeric", DfType, [])
def dfSelectNumeric(*args):
    df = getVars(args)["_parent_"]
    df = df.select_dtypes(include=[np.number])
    return fromDFtoObj("", df)


@makeMethod("fillna_median", DfType, [])
def dfFillnaMedian(*args):
    df = getVars(args)["_parent_"]
    df = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].apply(lambda s: s.fillna(s.median()))
    return fromDFtoObj("", df)


@makeMethod("select_cols", DfType, ["cols"])
def dfSelectCols(*args, **kwargs):
    vs = getVars(args, kwargs)
    df = vs["_parent_"]

    cols = vs.get("cols", [])
    if not isinstance(cols, list):
        cols = [cols]
    cols = [str(col.get() if hasattr(col, "get") else col) for col in cols]

    selected = [col for col in cols if col in df.columns]
    if len(selected) == 0:
        raise ValueError("select_cols: no matching columns")

    df = df[selected]
    return fromDFtoObj("", df)
