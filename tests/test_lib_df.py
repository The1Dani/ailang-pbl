"""
Tests for ailang/lib/AiLangBuiltinDfLib.py

Covers: dropna, dropna_ip
"""

import pandas as pd
import ailang.lib.AiLangLib as _

from ailang.engine.AiLangFunc import MethodSpace
from ailang.engine.AiLangObj import AiLangObj, fromDFtoObj
from ailang.engine.AiLangType import BasicListType, StrType
from ailang.engine.AiLangFunc import FunctionSpace


def dfWithNa() -> pd.DataFrame:
    """3-row DataFrame where row 1 has an NA value."""
    return pd.DataFrame({"a": [1.0, None, 3.0], "b": [4.0, 5.0, 6.0]})


def makeDfObj(df: pd.DataFrame) -> AiLangObj:
    """Build a full DfType AiLangObj with column members (as fromDFtoObj does)."""
    return fromDFtoObj("df", df)


# ---------------------------------------------------------------------------
# dropna
# ---------------------------------------------------------------------------


def testDropnaRemovesNaRows():
    df = dfWithNa()
    parent = makeDfObj(df)
    result = MethodSpace().call(parent, "dropna", [], {})
    result_df = result.get().get()
    assert len(result_df) == 2


def testDropnaDoesNotModifyParent():
    df = dfWithNa()
    parent = makeDfObj(df)
    original_len = len(parent.get().get())
    MethodSpace().call(parent, "dropna", [], {})
    assert len(parent.get().get()) == original_len


# ---------------------------------------------------------------------------
# dropna_ip
# ---------------------------------------------------------------------------


def testDropnaIpRemovesNaRows():
    df = dfWithNa()
    parent = makeDfObj(df)
    result = MethodSpace().call(parent, "dropna_ip", [], {})
    result_df = result.get().get()
    assert len(result_df) == 2


def testDropnaIpResultContainsNoNa():
    """dropna_ip result must have zero NA cells."""
    df = dfWithNa()
    parent = makeDfObj(df)
    result = MethodSpace().call(parent, "dropna_ip", [], {})
    result_df = result.get().get()
    assert result_df.isna().sum().sum() == 0


# ---------------------------------------------------------------------------
# map_bool_cols
# ---------------------------------------------------------------------------


def testMapBoolColsKeepsColumnMembersAccessible():
    df = pd.DataFrame({"flag": [True, False, True], "value": [1, 2, 3]})
    parent = makeDfObj(df)

    result = MethodSpace().call(
        parent,
        "map_bool_cols",
        [AiLangObj("cols", BasicListType(["flag"]))],
        {},
    )

    updated_df = result.get().get()
    assert updated_df["flag"].tolist() == [1, 0, 1]

    flag_member = result.getMember("flag")
    assert flag_member is not None
    assert flag_member.get().get().tolist() == [1, 0, 1]


def testSaveCsvWritesPredictions(tmp_path):
    out_file = tmp_path / "predictions.csv"
    FunctionSpace().call(
        "save_csv",
        [AiLangObj("data", BasicListType([1, 0, 1])), AiLangObj("path", StrType(str(out_file)))],
        {"ids": AiLangObj("ids", BasicListType([101, 102, 103]))},
    )
    saved = pd.read_csv(out_file)
    assert saved["prediction"].tolist() == [1, 0, 1]
