from typing import Any, cast

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score

from catboost import Pool

import numpy as np

from AiLangFunc import makeFunc
from AiLangObj import AiLangObj
from AiLangType import NumType, NumTypes, ListType, NoneType
from FuncUtils import getVars
from protocols import (
    SklearnClassifier,
    SklearnLinearRegressor,
    SklearnSVC,
    SklearnSVR,
    SklearnRandomForest,
    SklearnKNN,
    CatBoostModel,
    NumpyArrayLike,
)


# -----------------------------
# Logistic Regression
# -----------------------------
@makeFunc("predict_proba_logistic", ["model", "x"])
def predictProbaLogistic(*args, **kwargs):
    vs = getVars(args, kwargs)

    model: Any = vs["model"]
    x: Any = vs["x"]

    if isinstance(model, AiLangObj):
        model = model.get()

    if isinstance(x, AiLangObj):
        x = x.get()

    clf = cast(SklearnClassifier, model)
    proba: NumpyArrayLike = clf.predict_proba(cast(Any, x))

    return AiLangObj("proba", ListType(proba.tolist()))


@makeFunc("get_coef_table", ["model", "feature_names"])
def getCoefTable(*args, **kwargs):
    vs = getVars(args, kwargs)

    model: Any = vs["model"]
    feature_names: Any = vs["feature_names"]

    if isinstance(model, AiLangObj):
        model = model.get()

    if isinstance(feature_names, AiLangObj):
        feature_names = feature_names.get()

    regressor = cast(SklearnLinearRegressor, model)
    coefs: NumpyArrayLike = regressor.coef_

    table: list[list[Any]] = []
    for name, coef in zip(cast(Any, feature_names), cast(Any, coefs)):
        table.append([name, float(cast(Any, coef))])

    return AiLangObj("coef_table", ListType(table))


# -----------------------------
# Linear Regression
# -----------------------------


@makeFunc("residuals", ["y_true", "y_pred"])
def residuals(*args, **kwargs):
    vs = getVars(args, kwargs)

    y_true: Any = vs["y_true"]
    y_pred: Any = vs["y_pred"]

    if isinstance(y_true, AiLangObj):
        y_true = y_true.get()

    if isinstance(y_pred, AiLangObj):
        y_pred = y_pred.get()

    y_true_arr = cast(NumpyArrayLike, y_true)
    y_pred_arr = cast(NumpyArrayLike, y_pred)
    res: list[Any] = (y_true_arr - y_pred_arr).tolist()

    return AiLangObj("residuals", ListType(res))


@makeFunc("score_r2", ["model", "x_test", "y_test"])
def scoreR2(*args, **kwargs):
    vs = getVars(args, kwargs)

    model: Any = vs["model"]
    x_test: Any = vs["x_test"]
    y_test: Any = vs["y_test"]

    if isinstance(model, AiLangObj):
        model = model.get()

    if isinstance(x_test, AiLangObj):
        x_test = x_test.get()

    if isinstance(y_test, AiLangObj):
        y_test = y_test.get()

    predictor = cast(SklearnLinearRegressor, model)
    pred: NumpyArrayLike = predictor.predict(cast(Any, x_test))
    score = r2_score(cast(Any, y_test), cast(Any, pred))

    return AiLangObj("r2", NumType(score, NumTypes.FLOAT))


# -----------------------------
# Support Vector classifier (SVc)
# -----------------------------
@makeFunc("get_support_vectors", ["model"])
def getSupportVectors(*args, **kwargs):
    vs = getVars(args, kwargs)

    model: Any = vs["model"]

    if isinstance(model, AiLangObj):
        model = model.get()

    svc = cast(SklearnSVC, model)
    sv: NumpyArrayLike = svc.support_vectors_

    return AiLangObj("support_vectors", ListType(sv.tolist()))


@makeFunc("predict_proba_svc", ["model", "x"])
def predictProbaSVC(*args, **kwargs):
    vs = getVars(args, kwargs)

    model: Any = vs["model"]
    x: Any = vs["x"]

    if isinstance(model, AiLangObj):
        model = model.get()

    if isinstance(x, AiLangObj):
        x = x.get()

    if not hasattr(model, "predict_proba"):
        raise ValueError("SVC model not calibrated for probabilities")

    svc = cast(SklearnSVC, model)
    proba: NumpyArrayLike = svc.predict_proba(cast(Any, x))

    return AiLangObj("svc_proba", ListType(proba.tolist()))


# -----------------------------
# Support Vector Regressor (SVR)
# -----------------------------
@makeFunc("get_epsilon_band", ["model"])
def getEpsilonBand(*args, **kwargs):
    vs = getVars(args, kwargs)

    model: Any = vs["model"]

    if isinstance(model, AiLangObj):
        model = model.get()

    svr = cast(SklearnSVR, model)
    eps: float = svr.epsilon

    return AiLangObj("epsilon", NumType(eps, NumTypes.FLOAT))


# -----------------------------
# Random Forest
# -----------------------------


@makeFunc("get_feature_importance", ["model", "feature_names", "top_n"])
def aiLangGetFeatureImportanceRF(*args, **kwargs) -> AiLangObj:
    vs = getVars(args, kwargs)

    model_obj = vs["model"]
    feature_names = vs.get("feature_names")
    top_n = vs.get("top_n")

    model = model_obj.getMember("model").get()
    rf_model = cast(SklearnRandomForest, model)
    importances: NumpyArrayLike = rf_model.feature_importances_

    if feature_names is None:
        feature_names = [f"feature_{i}" for i in range(len(importances))]

    paired = sorted(
        zip(cast(Any, feature_names), importances.tolist()),
        key=lambda x: x[1],
        reverse=True,
    )

    if top_n is not None:
        paired = paired[: int(top_n)]

    result_list = ListType(
        [{"feature": f, "importance": round(v, 6)} for f, v in paired]
    )

    result = AiLangObj("result", NoneType())
    result.setMember(AiLangObj("importance_df", result_list))

    return result


# -----------------------------
# catBoost
# -----------------------------
@makeFunc("to_catboost_pool", ["x", "y", "cat_features"])
def toCatboostPool(*args, **kwargs):
    vs = getVars(args, kwargs)

    x = vs["x"]
    y = vs["y"]
    cat_features = vs.get("cat_features")

    if isinstance(x, AiLangObj):
        x = x.get()
    if isinstance(y, AiLangObj):
        y = y.get()

    pool = Pool(data=x, label=y, cat_features=cat_features)

    return AiLangObj("catboost_pool", pool)


@makeFunc("get_feature_importance_catboost", ["model", "importance_type", "x"])
def aiLangGetFeatureImportancecatBoost(*args, **kwargs) -> AiLangObj:
    vs = getVars(args, kwargs)

    model_obj = vs["model"]
    importance_type = vs.get("importance_type", "PredictionValuesChange")
    x = vs.get("x")

    # ---- get model safely ----
    model = model_obj.getMember("model").get()
    cb_model = cast(CatBoostModel, model)

    # ---- compute importances ----
    shap_values: list[Any] = []
    importances: list[Any] = []

    if importance_type == "ShapValues" and x is not None:

        raw_shap = cb_model.get_feature_importance(data=x, type="ShapValues")
        shap_values = raw_shap.tolist()

        # exclude last column (expected value)
        importances = np.abs(raw_shap[:, :-1]).mean(axis=0).tolist()

    else:
        importances = cb_model.get_feature_importance(type=importance_type).tolist()

    # ---- feature names ----
    feature_names: list[str] | None = cb_model.feature_names_

    paired = sorted(
        zip(cast(Any, feature_names), importances),
        key=lambda v: v[1],
        reverse=True,
    )

    # ---- wrap importance list ----
    importance_list = ListType(
        [{"feature": f, "importance": round(v, 6)} for f, v in paired]
    )

    result = AiLangObj("result", NoneType())

    result.setMember(AiLangObj("importance_df", importance_list))

    # ---- wrap shap values only if present ----
    if shap_values:
        result.setMember(AiLangObj("shap_values", ListType(shap_values)))

    return result


@makeFunc("get_shap_values", ["model", "x"])
def getShapValues(*args, **kwargs):
    vs = getVars(args, kwargs)

    model: Any = vs["model"]
    x: Any = vs["x"]

    if isinstance(model, AiLangObj):
        model = model.get()

    if isinstance(x, AiLangObj):
        x = x.get()

    cb_model = cast(CatBoostModel, model)
    shap_vals: NumpyArrayLike = cb_model.get_feature_importance(
        data=x, type="ShapValues"
    )

    return AiLangObj("shap_values", ListType(shap_vals.tolist()))


# -----------------------------
# K-Nearest Neighbors
# -----------------------------
@makeFunc("find_optimal_k", ["x", "y", "k_range", "cv", "metric"])
def aiLangFindOptimalK(*args, **kwargs) -> AiLangObj:  # pylint: disable=too-many-locals
    vs = getVars(args, kwargs)

    x = vs["x"]
    y = vs["y"]
    k_range = vs.get("k_range", list(range(1, 21)))
    cv = vs.get("cv", 5)
    metric = vs.get("metric", "accuracy")

    best_k = k_range[0]
    best_score = -np.inf

    scores_list = []

    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=int(k))
        scores = cross_val_score(knn, x, y, cv=int(cv), scoring=metric)

        mean_s = float(scores.mean())

        scores_list.append({"k": k, "score": round(mean_s, 6)})

        if mean_s > best_score:
            best_score = mean_s
            best_k = k

    result = AiLangObj("result", NoneType())

    result.setMember(AiLangObj("best_k", NumType(int(best_k), NumTypes.INT)))
    result.setMember(AiLangObj("cv_scores", ListType(scores_list)))
    return result


@makeFunc("get_neighbors", ["model", "x_query"])
def getNeighbors(*args, **kwargs):
    vs = getVars(args, kwargs)

    model: Any = vs["model"]
    x_query: Any = vs["x_query"]

    if isinstance(model, AiLangObj):
        model = model.get()

    if isinstance(x_query, AiLangObj):
        x_query = x_query.get()

    knn = cast(SklearnKNN, model)
    distances: NumpyArrayLike
    indices: NumpyArrayLike
    distances, indices = knn.kneighbors(cast(Any, x_query))

    return AiLangObj("neighbors", ListType([distances.tolist(), indices.tolist()]))
