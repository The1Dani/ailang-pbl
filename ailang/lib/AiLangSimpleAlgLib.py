from typing import Any

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn import metrics as sklearn_metrics

from catboost import Pool

import numpy as np

from ailang.engine.AiLangFunc import makeFunc, makeMethod
from ailang.engine.AiLangObj import AiLangObj
from ailang.engine.AiLangType import NumType, NumTypes, ListType, NoneType, PyType

from .FuncUtils import getVars


def unwrap(value: Any) -> Any:
    if isinstance(value, AiLangObj):
        return value.get()
    return value

def requireAttr(obj: Any, attr: str) -> None:
    if not hasattr(obj, attr):
        raise ValueError(f"Object does not support '{attr}'")

def toListObj(name: str, arr: np.ndarray) -> AiLangObj:
    return AiLangObj(name, ListType(arr.tolist()))

def toNumObj(name: str, value: float) -> AiLangObj:
    return AiLangObj(name, NumType(float(value), NumTypes.FLOAT))

# TODO: Decide What to do with this file

# ─────────────────────────────────────────────
# Prediction
# ─────────────────────────────────────────────
@makeMethod("predict", PyType, ["x"])
def predict(*args, **kwargs):
    vs = getVars(args, kwargs)
    model = unwrap(vs["_parent_"])
    x = unwrap(vs["x"])
    requireAttr(model, "predict")
    pred = model.predict(x)
    return toListObj("predictions", np.asarray(pred))

# ─────────────────────────────────────────────
# Evaluation
# ─────────────────────────────────────────────

_METRIC_FNS = {
    "r2":       sklearn_metrics.r2_score,
    "accuracy": sklearn_metrics.accuracy_score,
    "mse":      sklearn_metrics.mean_squared_error,
    "mae":      sklearn_metrics.mean_absolute_error,
}

@makeFunc("metric_score", ["y_true", "y_pred", "metric"])
def metricScore(*args, **kwargs):
    vs = getVars(args, kwargs)
    y_true = unwrap(vs["y_true"])
    y_pred = unwrap(vs["y_pred"])
    metric = unwrap(vs["metric"])

    fn = _METRIC_FNS.get(str(metric).lower())
    if fn is None:
        raise ValueError(
            f"Unknown metric '{metric}'. Supported: {list(_METRIC_FNS)}"
        )

    score = fn(y_true, y_pred)
    return toNumObj(f"{metric}_score", float(score))

# ─────────────────────────────────────────────
# Coefficients
# ─────────────────────────────────────────────

@makeMethod("get_coefficients", PyType, ["feature_names"])
def getCoefficients(*args, **kwargs):
    vs = getVars(args, kwargs)
    model = unwrap(vs["_parent_"])
    feature_names = unwrap(vs["feature_names"])

    requireAttr(model, "coef_")
    coefs = np.asarray(model.coef_).ravel()

    table = [
        {"feature": name, "coefficient": float(coef)}
        for name, coef in zip(feature_names, coefs)
    ]
    return AiLangObj("coef_table", ListType(table))

# ─────────────────────────────────────────────
# Residuals
# ─────────────────────────────────────────────

@makeMethod("residuals", ListType, ["y_pred"])
def residuals(*args, **kwargs):
    vs = getVars(args, kwargs)
    y_true = np.asarray(unwrap(vs["_parent_"]))
    y_pred = np.asarray(unwrap(vs["y_pred"]))
    return AiLangObj("residuals", ListType((y_true - y_pred).tolist()))

# -----------------------------
# Support Vector classifier (SVc)
# -----------------------------

@makeMethod("get_support_vectors", PyType, [])
def getSupportVectors(*args, **kwargs):
    vs = getVars(args, kwargs)
    model = unwrap(vs["_parent_"])

    requireAttr(model, "support_vectors_")
    return toListObj("support_vectors", model.support_vectors_)


# -----------------------------
# Support Vector Regressor (SVR)
# -----------------------------
@makeMethod("get_epsilon_band", PyType, [])
def getEpsilonBand(*args, **kwargs):
    vs = getVars(args, kwargs)
    model = unwrap(vs["_parent_"])

    requireAttr(model, "epsilon")
    return toNumObj("epsilon", model.epsilon)

# ─────────────────────────────────────────────
# Feature importance  (generic: RF, linear, CatBoost, …)
# ─────────────────────────────────────────────
def _computeImportances(model: Any, feature_names: list, top_n: int | None) -> list:
    if hasattr(model, "feature_importances_"):
        importances = np.asarray(model.feature_importances_)
    elif hasattr(model, "coef_"):
        importances = np.abs(np.asarray(model.coef_).ravel())
    else:
        raise ValueError("Model exposes neither 'feature_importances_' nor 'coef_'")

    paired = sorted(
        zip(feature_names, importances.tolist()),
        key=lambda item: item[1],
        reverse=True,
    )
    if top_n is not None:
        paired = paired[:int(top_n)]
    return [{"feature": f, "importance": round(v, 6)} for f, v in paired]

@makeMethod("feature_importance", PyType, ["feature_names", "top_n"])
def featureImportance(*args, **kwargs):
    vs = getVars(args, kwargs)
    model = unwrap(vs["_parent_"])
    feature_names = unwrap(vs.get("feature_names")) or [
        f"feature_{i}" for i in range(
            len(model.feature_importances_)
            if hasattr(model, "feature_importances_")
            else len(np.asarray(model.coef_).ravel())
        )
    ]
    top_n = vs.get("top_n")

    importance_list = _computeImportances(model, feature_names, top_n)

    result = AiLangObj("result", NoneType())
    result.setMember(AiLangObj("importance_df", ListType(importance_list)))
    return result

# ─────────────────────────────────────────────
# SHAP values (CatBoost or any compatible model)
# ─────────────────────────────────────────────

@makeMethod("shap_values", PyType, ["x"])
def shapValues(*args, **kwargs):
    vs = getVars(args, kwargs)
    model = unwrap(vs["_parent_"])
    x = unwrap(vs["x"])

    requireAttr(model, "get_feature_importance")
    shap_vals = model.get_feature_importance(data=x, type="ShapValues")
    return toListObj("shap_values", shap_vals)


# -----------------------------
# catBoost
# -----------------------------
@makeFunc("to_catboost_pool", ["x", "y", "cat_features"])
def toCatboostPool(*args, **kwargs):
    vs = getVars(args, kwargs)
    x = unwrap(vs["x"])
    y = unwrap(vs["y"])
    cat_features = vs.get("cat_features")

    pool = Pool(data=x, label=y, cat_features=cat_features)
    return AiLangObj("catboost_pool", pool)

# -----------------------------
# K-Nearest Neighbors
# -----------------------------

@makeMethod("get_neighbors", PyType, ["x_query"])
def getNeighbors(*args, **kwargs):
    vs = getVars(args, kwargs)
    model = unwrap(vs["_parent_"])
    x_query = unwrap(vs["x_query"])

    requireAttr(model, "kneighbors")
    distances, indices = model.kneighbors(x_query)
    return AiLangObj("neighbors", ListType([distances.tolist(), indices.tolist()]))


@makeFunc("find_optimal_k", ["x", "y", "k_range", "cv", "metric"])
def aiLangFindOptimalK(*args, **kwargs):  # pylint: disable=too-many-locals
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
        fold_scores = cross_val_score(knn, x, y, cv=int(cv), scoring=metric)
        mean_s = float(fold_scores.mean())
        scores_list.append({"k": k, "score": round(mean_s, 6)})

        if mean_s > best_score:
            best_score = mean_s
            best_k = k

    result = AiLangObj("result", NoneType())
    result.setMember(AiLangObj("best_k", NumType(int(best_k), NumTypes.INT)))
    result.setMember(AiLangObj("cv_scores", ListType(scores_list)))
    return result
