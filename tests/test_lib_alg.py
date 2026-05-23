"""
Tests for ailang/lib/AiLangSimpleAlgLib.py

Covers: metric_score, get_coefficients, residuals, get_support_vectors,
        get_epsilon_band, feature_importance, find_optimal_k, get_neighbors,
        to_catboost_pool, shap_values.
"""

import pytest
from catboost import Pool

import ailang.lib.AiLangLib as _  # noqa: F401

from ailang.engine.AiLangFunc import FunctionSpace, MethodSpace
from ailang.engine.AiLangObj import AiLangObj
from ailang.engine.AiLangType import ListType, NumType, NumTypes, PyType

from tests.conftest import makeList, makeNum, makeStr

# ---------------------------------------------------------------------------
# metric_score
# ---------------------------------------------------------------------------


def testMetricScoreAccuracyPerfect():
    y_true = makeList([0, 1, 1, 0])
    y_pred = makeList([0, 1, 1, 0])
    result = FunctionSpace().call(
        "metric_score", [y_true, y_pred, makeStr("accuracy")], {}
    )
    assert result.get().get() == pytest.approx(1.0)


def testMetricScoreAccuracyPartial():
    y_true = makeList([0, 1, 1])
    y_pred = makeList([0, 1, 0])
    result = FunctionSpace().call(
        "metric_score", [y_true, y_pred, makeStr("accuracy")], {}
    )
    assert result.get().get() == pytest.approx(2 / 3)


def testMetricScoreR2Perfect():
    y_true = makeList([1.0, 2.0, 3.0, 4.0])
    y_pred = makeList([1.0, 2.0, 3.0, 4.0])
    result = FunctionSpace().call("metric_score", [y_true, y_pred, makeStr("r2")], {})
    assert result.get().get() == pytest.approx(1.0)


def testMetricScoreMseZero():
    y_true = makeList([1.0, 2.0, 3.0])
    y_pred = makeList([1.0, 2.0, 3.0])
    result = FunctionSpace().call("metric_score", [y_true, y_pred, makeStr("mse")], {})
    assert result.get().get() == pytest.approx(0.0)


def testMetricScoreMaeZero():
    y_true = makeList([1.0, 2.0, 3.0])
    y_pred = makeList([1.0, 2.0, 3.0])
    result = FunctionSpace().call("metric_score", [y_true, y_pred, makeStr("mae")], {})
    assert result.get().get() == pytest.approx(0.0)


def testMetricScoreUnknownMetricRaises():
    y_true = makeList([1, 2, 3])
    y_pred = makeList([1, 2, 3])
    with pytest.raises(ValueError, match="Unknown metric"):
        FunctionSpace().call("metric_score", [y_true, y_pred, makeStr("blorp")], {})


# ---------------------------------------------------------------------------
# get_coefficients
# ---------------------------------------------------------------------------


def testGetCoefficientsLength(trainedClf, clfData):
    x, _ = clfData
    n_features = x.shape[1]
    feature_names = makeList([f"f{i}" for i in range(n_features)])
    result = MethodSpace().call(trainedClf, "get_coefficients", [feature_names], {})
    assert isinstance(result.val, ListType)
    coef_list = result.get().get()
    assert len(coef_list) == n_features


def testGetCoefficientsKeys(trainedClf, clfData):
    x, _ = clfData
    feature_names = makeList([f"f{i}" for i in range(x.shape[1])])
    result = MethodSpace().call(trainedClf, "get_coefficients", [feature_names], {})
    for item in result.get().get():
        assert "feature" in item
        assert "coefficient" in item


# ---------------------------------------------------------------------------
# residuals
# ---------------------------------------------------------------------------


def testResidualsValues():
    y_true_obj = AiLangObj("", ListType([3.0, 5.0, 7.0]))
    y_pred = makeList([1.0, 2.0, 3.0])
    result = MethodSpace().call(y_true_obj, "residuals", [y_pred], {})
    assert isinstance(result.val, ListType)
    vals = result.get().get()
    assert vals == pytest.approx([2.0, 3.0, 4.0])


# ---------------------------------------------------------------------------
# get_support_vectors
# ---------------------------------------------------------------------------


def testGetSupportVectorsNonempty(trainedSvc):
    result = MethodSpace().call(trainedSvc, "get_support_vectors", [], {})
    assert isinstance(result.val, ListType)
    assert len(result.get().get()) > 0


# ---------------------------------------------------------------------------
# get_epsilon_band
# ---------------------------------------------------------------------------


def testGetEpsilonBandPositive(trainedSvr):
    result = MethodSpace().call(trainedSvr, "get_epsilon_band", [], {})
    assert isinstance(result.val, NumType)
    assert result.get().get() > 0


# ---------------------------------------------------------------------------
# feature_importance
# ---------------------------------------------------------------------------


def testFeatureImportanceRfHasImportanceDf(trainedRf, clfData):
    x, _ = clfData
    feature_names = makeList([f"f{i}" for i in range(x.shape[1])])
    result = MethodSpace().call(
        trainedRf, "feature_importance", [feature_names, makeNum(x.shape[1])], {}
    )
    member = result.getMember("importance_df")
    assert member is not None
    assert len(member.get().get()) == x.shape[1]


def testFeatureImportanceLinearCoefFallback(trainedClf, clfData):
    """LogisticRegression has coef_ not feature_importances_ — should not raise."""
    x, _ = clfData
    feature_names = makeList([f"f{i}" for i in range(x.shape[1])])
    result = MethodSpace().call(
        trainedClf, "feature_importance", [feature_names, makeNum(x.shape[1])], {}
    )
    member = result.getMember("importance_df")
    assert member is not None


# ---------------------------------------------------------------------------
# find_optimal_k
# ---------------------------------------------------------------------------


def testFindOptimalKReturnsBestK(clfData):
    x, y = clfData
    k_range = list(range(1, 6))
    result = FunctionSpace().call(
        "find_optimal_k",
        [
            makeList(x.tolist()),
            makeList(y.tolist()),
            makeList(k_range),
            makeNum(3, NumTypes.INT),
            makeStr("accuracy"),
        ],
        {},
    )
    best_k_obj = result.getMember("best_k")
    assert best_k_obj is not None
    best_k = best_k_obj.get().get()
    assert int(best_k) in k_range


def testFindOptimalKCvScoresLength(clfData):
    x, y = clfData
    k_range = list(range(1, 6))
    result = FunctionSpace().call(
        "find_optimal_k",
        [
            makeList(x.tolist()),
            makeList(y.tolist()),
            makeList(k_range),
            makeNum(3, NumTypes.INT),
            makeStr("accuracy"),
        ],
        {},
    )
    cv_scores_obj = result.getMember("cv_scores")
    assert cv_scores_obj is not None
    assert len(cv_scores_obj.get().get()) == len(k_range)


# ---------------------------------------------------------------------------
# get_neighbors
# ---------------------------------------------------------------------------


def testGetNeighborsReturnsDistancesAndIndices(trainedKnn, clfData):
    x, _ = clfData
    query = makeList(x[:2].tolist())
    result = MethodSpace().call(trainedKnn, "get_neighbors", [query], {})
    assert isinstance(result.val, ListType)
    payload = result.get().get()
    assert len(payload) == 2


# ---------------------------------------------------------------------------
# to_catboost_pool
# ---------------------------------------------------------------------------


def testToCatboostPoolType(clfData):
    x, y = clfData
    result = FunctionSpace().call(
        "to_catboost_pool",
        [makeList(x.tolist()), makeList(y.tolist()), makeList([])],
        {},
    )
    assert isinstance(result.get(), Pool)


# ---------------------------------------------------------------------------
# shap_values
# ---------------------------------------------------------------------------


def testShapValuesShape(trainedCatboost, clfData):
    x, y = clfData
    pool = Pool(x, y)

    result = MethodSpace().call(
        trainedCatboost, "shap_values", [AiLangObj("x", PyType(pool))], {}
    )
    assert isinstance(result.val, ListType)
    shap_matrix = result.get().get()
    assert len(shap_matrix) == len(x)
