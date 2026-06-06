import pandas as pd
import numpy as np

from ailang.engine.AiLangFunc import makeMethod, makeFunc
from ailang.engine.AiLangObj import AiLangObj, fromDFtoObj
from ailang.engine.AiLangType import DfType, ListType
from .FuncUtils import getVars


def getDf(parent: AiLangObj | pd.DataFrame) -> pd.DataFrame:
    if isinstance(parent, pd.DataFrame):
        return parent
    if not isinstance(parent, AiLangObj):
        raise ValueError()
    df = parent.get().get()
    if not isinstance(df, pd.DataFrame):
        raise ValueError()
    return df


def updateDfObj(parent_obj: AiLangObj, df: pd.DataFrame) -> AiLangObj:
    target = parent_obj.original_reference or parent_obj
    target.update(fromDFtoObj(target.ident, df))
    return target


@makeFunc("df_col", ["df", "col"])
def dfCol(*args, **kwargs):
    vs = getVars(args, kwargs)
    df = getDf(vs["df"])
    col = vs["col"]
    if hasattr(col, "get"):
        col = col.get()
    col = str(col)
    if col not in df.columns:
        raise ValueError(f"Column not found: {col}")
    return AiLangObj("col", ListType(df[col].tolist()))


@makeMethod("dropna_ip", DfType, [])
def dfBuiltinDropnaInplace(parent, *items):
    df = getDf(parent)

    df = df.dropna(*items)
    return updateDfObj(parent, df)


@makeMethod("dropna", DfType, [])
def dfBuiltinDropna(parent, *items):
    df = getDf(parent)

    df = df.dropna(*items)

    return fromDFtoObj(parent.ident, df)


# vs["_parent_"]
@makeMethod("map_bool_cols", DfType, ["cols"])
def dfMapBoolCols(*args, **kwargs):
    vs = getVars(args, kwargs)
    parent_obj = args[0]
    df = getDf(parent_obj)

    cols = vs.get("cols", [])
    if not isinstance(cols, list):
        cols = [cols]
    cols = [str(col.get() if hasattr(col, "get") else col) for col in cols]

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

    return fromDFtoObj(parent_obj.ident, df)


@makeMethod("select_numeric", DfType, [])
def dfSelectNumeric(parent, *args, **kwargs):  # pylint: disable=unused-argument
    df = getDf(parent)
    df = df.select_dtypes(include=[np.number])
    return fromDFtoObj(parent.ident, df)


@makeMethod("fillna_median", DfType, [])
def dfFillnaMedian(parent, *args, **kwargs):  # pylint: disable=unused-argument
    df = getDf(parent)
    df = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].apply(lambda s: s.fillna(s.median()))
    return fromDFtoObj(parent.ident, df)


@makeMethod("select_cols", DfType, ["cols"])
def dfSelectCols(*args, **kwargs):
    vs = getVars(args, kwargs)
    parent_obj = args[0]
    df = getDf(parent_obj)

    cols = vs.get("cols", [])
    if not isinstance(cols, list):
        cols = [cols]
    cols = [str(col.get() if hasattr(col, "get") else col) for col in cols]

    selected = [col for col in cols if col in df.columns]
    if len(selected) == 0:
        raise ValueError("select_cols: no matching columns")

    df = df[selected]
    return fromDFtoObj(parent_obj.ident, df)
