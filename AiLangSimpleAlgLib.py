from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score

from catboost import Pool

import numpy as np

from AiLangFunc import makeFunc
from AiLangObj import AiLangObj
from AiLangType import NumType, NumTypes, BasicListType, NoneType


def unwrap(value):
    if isinstance(value, AiLangObj):
        value = value.get()
    if hasattr(value, "get"):
        value = value.get()
    return value


# -----------------------------
# Logistic Regression
# -----------------------------
@makeFunc("predict_proba_logistic")
def predictProbaLogistic(*items):
    model = items[0]
    x = items[1]

    if isinstance(model, AiLangObj):
        model = model.get()

    if isinstance(x, AiLangObj):
        x = x.get()

    proba = model.predict_proba(x)

    return AiLangObj(
        "proba",
        BasicListType(proba.tolist())
    )

@makeFunc("get_coef_table")
def getCoefTable(*items):
    model = items[0]
    feature_names = items[1]

    if isinstance(model, AiLangObj):
        model = model.get()

    if isinstance(feature_names, AiLangObj):
        feature_names = feature_names.get()

    coefs = model.coef_[0]

    table = []
    for name, coef in zip(feature_names, coefs):
        table.append([name, float(coef)])

    return AiLangObj("coef_table", BasicListType(table))

# -----------------------------
# Linear Regression
# -----------------------------


@makeFunc("residuals")
def residuals(*items):
    y_true = items[0]
    y_pred = items[1]

    if isinstance(y_true, AiLangObj):
        y_true = y_true.get()

    if isinstance(y_pred, AiLangObj):
        y_pred = y_pred.get()

    res = (y_true - y_pred).tolist()

    return AiLangObj("residuals", BasicListType(res))


@makeFunc("score_r2")
def scoreR2(*items):
    model = items[0]
    x_test = items[1]
    y_test = items[2]

    if isinstance(model, AiLangObj):
        model = model.get()

    if isinstance(x_test, AiLangObj):
        x_test = x_test.get()

    if isinstance(y_test, AiLangObj):
        y_test = y_test.get()

    pred = model.predict(x_test)
    score = r2_score(y_test, pred)

    return AiLangObj("r2", NumType(score, NumTypes.FLOAT))

# -----------------------------
# Support Vector classifier (SVc)
# -----------------------------
@makeFunc("get_support_vectors")
def getSupportVectors(*items):
    model = items[0]

    if isinstance(model, AiLangObj):
        model = model.get()

    sv = model.support_vectors_

    return AiLangObj("support_vectors", BasicListType(sv.tolist()))

@makeFunc("predict_proba_svc")
def predictProbaSVC(*items):
    model = items[0]
    x = items[1]

    if isinstance(model, AiLangObj):
        model = model.get()

    if isinstance(x, AiLangObj):
        x = x.get()

    if not hasattr(model, "predict_proba"):
        raise ValueError("SVC model not calibrated for probabilities")

    proba = model.predict_proba(x)

    return AiLangObj("svc_proba", BasicListType(proba.tolist()))

# -----------------------------
# Support Vector Regressor (SVR)
# -----------------------------
@makeFunc("get_epsilon_band")
def getEpsilonBand(*items):
    model = items[0]

    if isinstance(model, AiLangObj):
        model = model.get()

    eps = model.epsilon

    return AiLangObj("epsilon", NumType(eps, NumTypes.FLOAT))
# -----------------------------
# Random Forest
# -----------------------------

@makeFunc("get_feature_importance")
def aiLangGetFeatureImportanceRF(*items) -> AiLangObj:

    if len(items) < 1:
        raise ValueError()

    model_obj = unwrap(items[0])
    feature_names = unwrap(items[1]) if len(items) > 1 else None
    top_n = unwrap(items[2]) if len(items) > 2 else None

    model = model_obj.getMember("model").get()
    importances = model.feature_importances_

    if feature_names is None:
        feature_names = [f"feature_{i}" for i in range(len(importances))]

    paired = sorted(
        zip(feature_names, importances.tolist()),
        key=lambda x: x[1],
        reverse=True,
    )

    if top_n is not None:
        paired = paired[:int(top_n)]

    result_list = BasicListType([
        {"feature": f, "importance": round(v, 6)} for f, v in paired
    ])

    result = AiLangObj("result", NoneType())
    result.setMember(AiLangObj("importance_df", result_list))

    return result

# -----------------------------
# catBoost
# -----------------------------
@makeFunc("to_catboost_pool")
def toCatboostPool(*items):
    x = items[0]
    y = items[1]
    cat_features = items[2] if len(items) > 2 else None

    if isinstance(x, AiLangObj):
        x = x.get()
    if isinstance(y, AiLangObj):
        y = y.get()

    pool = Pool(data=x, label=y, cat_features=cat_features)

    return AiLangObj("catboost_pool", pool)

@makeFunc("get_feature_importance_catboost")
def aiLangGetFeatureImportancecatBoost(*items) -> AiLangObj:

    # ---- validate ----
    if len(items) < 1:
        raise ValueError()

    model_obj = unwrap(items[0])
    importance_type = unwrap(items[1]) if len(items) > 1 else "PredictionValuesChange"
    x = unwrap(items[2]) if len(items) > 2 else None

    # ---- get model safely ----
    model = model_obj.getMember("model").get()

    # ---- compute importances ----
    shap_values = []
    importances = []

    if importance_type == "ShapValues" and x is not None:

        raw_shap = model.get_feature_importance(data=x, type="ShapValues")
        shap_values = raw_shap.tolist()

        # exclude last column (expected value)
        importances = np.abs(raw_shap[:, :-1]).mean(axis=0).tolist()

    else:
        importances = model.get_feature_importance(type=importance_type).tolist()

    # ---- feature names ----
    feature_names = model.feature_names_

    paired = sorted(
        zip(feature_names, importances),
        key=lambda v: v[1],
        reverse=True,
    )

    # ---- wrap importance list ----
    importance_list = BasicListType([
        {"feature": f, "importance": round(v, 6)}
        for f, v in paired
    ])

    result = AiLangObj("result", NoneType())

    result.setMember(AiLangObj("importance_df", importance_list))

    # ---- wrap shap values only if present ----
    if shap_values:
        result.setMember(
            AiLangObj("shap_values", BasicListType(shap_values))
        )

    return result

@makeFunc("get_shap_values")
def getShapValues(*items):
    model = items[0]
    x = items[1]

    if isinstance(model, AiLangObj):
        model = model.get()

    if isinstance(x, AiLangObj):
        x = x.get()

    shap_vals = model.get_feature_importance(data=x, type="ShapValues")

    return AiLangObj("shap_values", BasicListType(shap_vals.tolist()))
# -----------------------------
# K-Nearest Neighbors
# -----------------------------
@makeFunc("find_optimal_k")
def aiLangFindOptimalK(*items) -> AiLangObj:

    if len(items) < 2:
        raise ValueError()

    x = unwrap(items[0])
    y = unwrap(items[1])

    k_range = unwrap(items[2]) if len(items) > 2 else list(range(1, 21))
    cv = unwrap(items[3]) if len(items) > 3 else 5
    metric = unwrap(items[4]) if len(items) > 4 else "accuracy"

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
    result.setMember(AiLangObj("cv_scores", BasicListType(scores_list)))
    return result

@makeFunc("get_neighbors")
def getNeighbors(*items):
    model = items[0]
    x_query = items[1]

    if isinstance(model, AiLangObj):
        model = model.get()

    if isinstance(x_query, AiLangObj):
        x_query = x_query.get()

    distances, indices = model.kneighbors(x_query)

    return AiLangObj("neighbors", BasicListType([
        distances.tolist(),
        indices.tolist()
    ]))