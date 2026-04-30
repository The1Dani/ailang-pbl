from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.svm import SVC, SVR
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.model_selection import cross_val_score

import numpy as np

from catboost import CatBoostClassifier, CatBoostRegressor

from AiLangFunc import makeFunc
from AiLangObj import AiLangObj
from AiLangType import NumType, NumTypes, BasicListType, NoneType, AiLangType


def unwrap(value):
    if isinstance(value, AiLangObj):
        value = value.get()
    if hasattr(value, "get"):
        value = value.get()
    return value


def _wrap(data: dict) -> AiLangObj:
    """Wrap a plain dict into an AiLangObj result."""
    return AiLangObj("result", AiLangType(data))


def _toList(arr) -> list:
    """convert numpy arrays / lists / None to plain Python list."""
    if arr is None:
        return []
    if hasattr(arr, "tolist"):
        return arr.tolist()
    return list(arr)


# -----------------------------
# Logistic Regression
# -----------------------------
@makeFunc("fit_logistic_regression")
def aiLangFitLogisticRegression(*items):
    # ---- argument validation ----
    if len(items) < 2:
        raise ValueError()

    x = unwrap(items[0])
    y = unwrap(items[1])

    penalty = unwrap(items[2]) if len(items) > 2 else "l2"
    c = unwrap(items[3]) if len(items) > 3 else 1.0
    max_iter = unwrap(items[4]) if len(items) > 4 else 100
    solver = unwrap(items[5]) if len(items) > 5 else "lbfgs"

    # create model
    model = LogisticRegression(
        penalty=penalty, C=float(c), max_iter=int(max_iter), solver=solver
    )
    # train model
    model.fit(x, y)

    # ---- wrap outputs properly ----
    coef = BasicListType(model.coef_.tolist())
    intercept = BasicListType(model.intercept_.tolist())

    result = AiLangObj("result", NoneType())

    result.setMember(AiLangObj("coef_", coef))
    result.setMember(AiLangObj("intercept_", intercept))

    # store model internally (opaque)
    result.setMember(AiLangObj("model", model))

    return result


@makeFunc("predict_logistic")
def aiLangPredictLogistic(*items):
    if len(items) < 2:
        raise ValueError()
    # unwrap parameters
    model_obj = unwrap(items[0])
    x = unwrap(items[1])

    model = model_obj.getMember("model").get()

    # make predictions
    y_pred = model.predict(x)
    y_proba = model.predict_proba(x)

    # return result
    result = AiLangObj("result", NoneType())
    result.setMember(AiLangObj("y_pred", y_pred))
    result.setMember(AiLangObj("y_proba", y_proba))

    return result


# -----------------------------
# Linear Regression
# -----------------------------


@makeFunc("fit_linear_regression")
def aiLangFitLinearRegression(*items) -> AiLangObj:
    if len(items) < 2:
        raise ValueError()
    # unwrap parameters
    x = unwrap(items[0])
    y = unwrap(items[1])

    fit_intercept = unwrap(items[2]) if len(items) > 2 else True
    regularization = unwrap(items[3]) if len(items) > 3 else "none"
    alpha = unwrap(items[4]) if len(items) > 4 else 1.0
    l1_ratio = unwrap(items[5]) if len(items) > 5 else 0.5

    reg = regularization.lower() if isinstance(regularization, str) else "none"

    if reg == "ridge":
        model = Ridge(alpha=float(alpha), fit_intercept=bool(fit_intercept))
    elif reg == "lasso":
        model = Lasso(alpha=float(alpha), fit_intercept=bool(fit_intercept))
    elif reg == "elasticnet":
        model = ElasticNet(
            alpha=float(alpha),
            l1_ratio=float(l1_ratio),
            fit_intercept=bool(fit_intercept),
        )
    else:
        model = LinearRegression(fit_intercept=bool(fit_intercept))

    model.fit(x, y)

      # ---- wrap outputs ----
    coef = BasicListType(model.coef_.tolist())

    # intercept can be scalar or array
    if np.ndim(model.intercept_) == 0:
        intercept = NumType(float(model.intercept_), NumTypes.FLOAT)
    else:
        intercept = BasicListType(model.intercept_.tolist())

    r2 = NumType(float(model.score(x, y)), NumTypes.FLOAT)

    # ---- build result object ----
    result = AiLangObj("result", NoneType())

    result.setMember(AiLangObj("coef_", coef))
    result.setMember(AiLangObj("intercept_", intercept))
    result.setMember(AiLangObj("r2_score", r2))

    # store model (opaque)
    result.setMember(AiLangObj("model", model))

    return result


@makeFunc("predict_linear")
def aiLangPredictLinear(*items)  -> AiLangObj:
    if len(items) < 2:
        raise ValueError()
    model_obj = unwrap(items[0])
    x = unwrap(items[1])

    # retrieve stored model
    model = model_obj.getMember("model").get()

    y_pred = model.predict(x)

    result = AiLangObj("result", NoneType())
    result.setMember(
        AiLangObj("y_pred", BasicListType(y_pred.tolist()))
    )

    return result


# -----------------------------
# Support Vector classifier (SVc)
# -----------------------------
@makeFunc("fit_svc")
def aiLangFitSVc(*items) -> AiLangObj:
    if len(items) < 2:
        raise ValueError()

    x = unwrap(items[0])
    y = unwrap(items[1])

    kernel = unwrap(items[2]) if len(items) > 2 else "rbf"
    c = unwrap(items[3]) if len(items) > 3 else 1.0
    gamma = unwrap(items[4]) if len(items) > 4 else "scale"
    degree = unwrap(items[5]) if len(items) > 5 else 3
    probability = unwrap(items[6]) if len(items) > 6 else False

    model = SVC(
        kernel=kernel,
        C=float(c),
        gamma=gamma,
        degree=int(degree),
        probability=bool(probability),
    )
    model.fit(x, y)

      # ---- wrap outputs ----
    support_vectors = BasicListType(model.support_vectors_.tolist())
    n_support = BasicListType(model.n_support_.tolist())

    result = AiLangObj("result", NoneType())

    result.setMember(AiLangObj("support_vectors_", support_vectors))
    result.setMember(AiLangObj("n_support_", n_support))

    # store model (opaque)
    result.setMember(AiLangObj("model", model))

    return result


@makeFunc("predict_svc")
def aiLangPredictSVc(*items) -> AiLangObj:

    if len(items) < 2:
        raise ValueError()

    model_obj = unwrap(items[0])
    x = unwrap(items[1])

     # retrieve model safely
    model = model_obj.getMember("model").get()

    y_pred = model.predict(x)
    decision_scores = model.decision_function(x)

    result = AiLangObj("result", NoneType())

    result.setMember(
        AiLangObj("y_pred", BasicListType(y_pred.tolist()))
    )

    result.setMember(
        AiLangObj("decision_scores", BasicListType(decision_scores.tolist()))
    )
    return result


# -----------------------------
# Support Vector Regressor (SVR)
# -----------------------------
@makeFunc("fit_svr")
def aiLangFitSVR(*items) -> AiLangObj:

    if len(items) < 2:
        raise ValueError()

    x = unwrap(items[0])
    y = unwrap(items[1])

    kernel = unwrap(items[2]) if len(items) > 2 else "rbf"
    c = unwrap(items[3]) if len(items) > 3 else 1.0
    epsilon = unwrap(items[4]) if len(items) > 4 else 0.1
    gamma = unwrap(items[5]) if len(items) > 5 else "scale"

    model = SVR(
        kernel=kernel,
        C=float(c),
        epsilon=float(epsilon),
        gamma=gamma
    )

    model.fit(x, y)

    result = AiLangObj("result", NoneType())

    result.setMember(
        AiLangObj("support_vectors_", BasicListType(model.support_vectors_.tolist()))
    )

    result.setMember(AiLangObj("model", model))

    return result

@makeFunc("predict_svr")
def aiLangPredictSVR(*items) -> AiLangObj:

    if len(items) < 2:
        raise ValueError()

    model_obj = unwrap(items[0])
    x = unwrap(items[1])

    model = model_obj.getMember("model").get()

    y_pred = model.predict(x)

    result = AiLangObj("result", NoneType())
    result.setMember(AiLangObj("y_pred", BasicListType(y_pred.tolist())))

    return result

# -----------------------------
# Random Forest
# -----------------------------
@makeFunc("fit_random_forest")
def aiLangFitRandomForest(*items) -> AiLangObj:

    if len(items) < 2:
        raise ValueError()

    x = unwrap(items[0])
    y = unwrap(items[1])

    task = unwrap(items[2]) if len(items) > 2 else "classification"
    n_estimators = unwrap(items[3]) if len(items) > 3 else 100
    max_depth = unwrap(items[4]) if len(items) > 4 else None
    max_features = unwrap(items[5]) if len(items) > 5 else "sqrt"
    min_samples_split = unwrap(items[6]) if len(items) > 6 else 2
    min_samples_leaf = unwrap(items[7]) if len(items) > 7 else 1
    bootstrap = unwrap(items[8]) if len(items) > 8 else True
    random_state = unwrap(items[9]) if len(items) > 9 else None
    n_jobs = unwrap(items[10]) if len(items) > 10 else -1

    kwargs = {
        "n_estimators": int(n_estimators),
        "max_depth": max_depth,
        "max_features": max_features,
        "min_samples_split": int(min_samples_split),
        "min_samples_leaf": int(min_samples_leaf),
        "bootstrap": bool(bootstrap),
        "oob_score": bool(bootstrap),
        "random_state": random_state,
        "n_jobs": int(n_jobs),
    }

    model = (
        RandomForestRegressor(**kwargs)
        if task == "regression"
        else RandomForestClassifier(**kwargs)
    )

    model.fit(x, y)

    result = AiLangObj("result", NoneType())

    result.setMember(
        AiLangObj("feature_importances_", BasicListType(model.feature_importances_.tolist()))
    )

    if bootstrap:
        result.setMember(
            AiLangObj("oob_score_", NumType(float(model.oob_score_), NumTypes.FLOAT))
        )

    result.setMember(AiLangObj("model", model))

    return result

@makeFunc("predict_random_forest")
def aiLangPredictRandomForest(*items) -> AiLangObj:

    if len(items) < 2:
        raise ValueError()

    model_obj = unwrap(items[0])
    x = unwrap(items[1])

    model = model_obj.getMember("model").get()

    result = AiLangObj("result", NoneType())

    result.setMember(
        AiLangObj("y_pred", BasicListType(model.predict(x).tolist()))
    )

    if hasattr(model, "predict_proba"):
        result.setMember(
            AiLangObj("y_proba", BasicListType(model.predict_proba(x).tolist()))
        )

    return result

@makeFunc("get_feature_importance_rf")
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
@makeFunc("fit_catboost")
def aiLangFitcatBoost(*items) -> AiLangObj:

    if len(items) < 2:
        raise ValueError()

    x = unwrap(items[0])
    y = unwrap(items[1])

    task = unwrap(items[2]) if len(items) > 2 else "classification"
    iterations = unwrap(items[3]) if len(items) > 3 else 1000
    depth = unwrap(items[4]) if len(items) > 4 else 6

    model = (
        CatBoostRegressor(iterations=iterations, depth=depth, verbose=0)
        if task == "regression"
        else CatBoostClassifier(iterations=iterations, depth=depth, verbose=0)
    )

    model.fit(x, y)

    result = AiLangObj("result", NoneType())

    result.setMember(
        AiLangObj("feature_importances_", BasicListType(model.feature_importances_.tolist()))
    )

    result.setMember(AiLangObj("model", model))

    return result

@makeFunc("predict_catboost")
def aiLangPredictcatBoost(*items) -> AiLangObj:

    if len(items) < 2:
        raise ValueError()

    model_obj = unwrap(items[0])
    x = unwrap(items[1])

    model = model_obj.getMember("model").get()

    result = AiLangObj("result", NoneType())

    result.setMember(
        AiLangObj("y_pred", BasicListType(model.predict(x).tolist()))
    )

    if isinstance(model, CatBoostClassifier):
        result.setMember(
            AiLangObj("y_proba", BasicListType(model.predict_proba(x).tolist()))
        )

    return result

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

# -----------------------------
# K-Nearest Neighbors
# -----------------------------
@makeFunc("fit_knn")
def aiLangFitKNN(*items) -> AiLangObj:

    if len(items) < 2:
        raise ValueError()

    x = unwrap(items[0])
    y = unwrap(items[1])

    task = unwrap(items[2]) if len(items) > 2 else "classification"
    k = unwrap(items[3]) if len(items) > 3 else 5

    model = (
        KNeighborsRegressor(n_neighbors=int(k))
        if task == "regression"
        else KNeighborsClassifier(n_neighbors=int(k))
    )

    model.fit(x, y)

    result = AiLangObj("result", NoneType())
    result.setMember(AiLangObj("model", model))

    return result

@makeFunc("predict_knn")
def aiLangPredictKNN(*items) -> AiLangObj:

    if len(items) < 2:
        raise ValueError()

    model_obj = unwrap(items[0])
    x = unwrap(items[1])

    model = model_obj.getMember("model").get()

    y_pred = model.predict(x)
    distances, indices = model.kneighbors(x)

    result = AiLangObj("result", NoneType())

    result.setMember(AiLangObj("y_pred", BasicListType(y_pred.tolist())))
    result.setMember(AiLangObj("neighbor_indices", BasicListType(indices.tolist())))
    result.setMember(AiLangObj("neighbor_distances", BasicListType(distances.tolist())))

    if hasattr(model, "predict_proba"):
        result.setMember(
            AiLangObj("y_proba", BasicListType(model.predict_proba(x).tolist()))
        )

    return result

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
