"""
Tests for ailang/lib/AiLangLib.py

Covers: fit, predict, score, cross_validate, train_test_split,
        save_model, load_model, print, exit (via FunctionSpace /
        MethodSpace).
"""

import copy
import math

import ailang.lib.AiLangLib as _  # noqa: F401

from ailang.engine.AiLangFunc import FunctionSpace, MethodSpace
from ailang.engine.AiLangObj import AiLangObj, NoneObj
from ailang.engine.AiLangType import BasicListType, NumType, NumTypes, PyType

from tests.conftest import makeList, makeNum, makeStr

# ---------------------------------------------------------------------------
# fit
# ---------------------------------------------------------------------------


def testFitReturnsAilangobjWithPytype(clfData):
    x, y = clfData
    parent = AiLangObj("logistic_regression")  # val defaults to None

    result = MethodSpace().call(
        parent,
        "fit",
        [makeList(x.tolist()), makeList(y.tolist())],
        {},
    )

    assert isinstance(result, AiLangObj)
    assert isinstance(result.val, PyType)


def testFitWithExistingPytypeParent(clfData, trainedClf):
    """Passing a PyType parent (already a model) re-fits it."""
    x, y = clfData
    fresh = copy.deepcopy(trainedClf)
    result = MethodSpace().call(
        fresh,
        "fit",
        [makeList(x.tolist()), makeList(y.tolist())],
        {},
    )
    assert isinstance(result.val, PyType)


# ---------------------------------------------------------------------------
# predict
# ---------------------------------------------------------------------------


def testPredictLengthMatchesInput(clfData, trainedClf):
    x, _ = clfData
    result = MethodSpace().call(
        trainedClf,
        "predict",
        [makeList(x.tolist())],
        {},
    )
    assert isinstance(result.val, BasicListType)
    assert len(result.get().get()) == len(x)


# ---------------------------------------------------------------------------
# score
# ---------------------------------------------------------------------------


def testScoreReturnsFloatInUnitInterval(clfData, trainedClf):
    x, y = clfData
    result = MethodSpace().call(
        trainedClf,
        "score",
        [makeList(x.tolist()), makeList(y.tolist())],
        {},
    )
    assert isinstance(result.val, NumType)
    score = result.get().get()
    assert 0.0 <= score <= 1.0


# ---------------------------------------------------------------------------
# cross_validate
# ---------------------------------------------------------------------------


def testCrossValidateHasScoresAndMeanScore(clfData):
    x, y = clfData
    parent = AiLangObj("logistic_regression")  # val = None

    result = MethodSpace().call(
        parent,
        "cross_validate",
        [
            makeList(x.tolist()),
            makeList(y.tolist()),
            makeNum(3, NumTypes.INT),
            makeStr("accuracy"),
        ],
        {},
    )

    assert result.getMember("scores") is not None
    assert result.getMember("mean_score") is not None


def testCrossValidateMeanScoreIsFloat(clfData):
    x, y = clfData
    parent = AiLangObj("logistic_regression")  # val = None

    result = MethodSpace().call(
        parent,
        "cross_validate",
        [
            makeList(x.tolist()),
            makeList(y.tolist()),
            makeNum(3, NumTypes.INT),
            makeStr("accuracy"),
        ],
        {},
    )

    mean_score_obj = result.getMember("mean_score")
    assert mean_score_obj is not None
    val = mean_score_obj.get().get()
    assert isinstance(val, float)
    assert not math.isnan(val)


# ---------------------------------------------------------------------------
# train_test_split
# ---------------------------------------------------------------------------


def testTrainTestSplitHasFourMembers(clfData):
    x, y = clfData
    result = FunctionSpace().call(
        "train_test_split",
        [makeList(x.tolist()), makeList(y.tolist()), makeNum(0.25)],
        {},
    )
    for name in ("X_train", "X_test", "y_train", "y_test"):
        assert result.getMember(name) is not None, f"Missing member: {name}"


def testTrainTestSplitSizes(clfData):
    x, y = clfData  # 40 rows
    result = FunctionSpace().call(
        "train_test_split",
        [makeList(x.tolist()), makeList(y.tolist()), makeNum(0.25)],
        {},
    )
    x_test_obj = result.getMember("X_test")
    assert x_test_obj is not None
    x_train_obj = result.getMember("X_train")
    assert x_train_obj is not None
    x_test = x_test_obj.get().get()
    x_train = x_train_obj.get().get()
    assert len(x_test) == 10
    assert len(x_train) == 30


# ---------------------------------------------------------------------------
# save_model / load_model
# ---------------------------------------------------------------------------


def testSaveLoadModelRoundtrip(tmp_path, trainedClf, clfData):
    path = str(tmp_path / "model.joblib")

    MethodSpace().call(trainedClf, "save_model", [makeStr(path)], {})

    result = FunctionSpace().call("load_model", [makeStr(path)], {})
    assert isinstance(result.val, PyType)

    x, _ = clfData
    preds = result.get().get().predict(x)
    assert len(preds) == len(x)


# ---------------------------------------------------------------------------
# print
# ---------------------------------------------------------------------------


def testPrintReturnsNoneobj(capsys):
    result = FunctionSpace().call("print", [makeStr("hello")], {})
    assert result is NoneObj()
    captured = capsys.readouterr()
    assert "hello" in captured.out
