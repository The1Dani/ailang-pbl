import sys
from AiLangFunc import makeFunc, makeMethod
from AiLangObj import AiLangObj, NoneObj
from AiLangType import AiLangType, NumType, NumTypes
import AiLangBuiltinDfLib as _

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.svm import SVC, SVR
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.model_selection import cross_val_score

import numpy as np

from catboost import CatBoostClassifier, CatBoostRegressor

def unwrap(value):
    if isinstance(value, AiLangObj):
        value = value.get()

    if isinstance(value, AiLangType):
        value = value.get()

    return value

def _wrap(data: dict) -> AiLangObj:
    """Wrap a plain dict into an AiLangObj result."""
    return AiLangObj("result", AiLangType(data))
 
 
def _to_list(arr) -> list:
    """Convert numpy arrays / lists / None to plain Python list."""
    if arr is None:
        return []
    if hasattr(arr, "tolist"):
        return arr.tolist()
    return list(arr)
@makeFunc("print")
def aiLangBuiltinPrint(*items: AiLangObj | AiLangType) -> AiLangObj:

    for item in items:
        if isinstance(item, AiLangObj):
            item = item.get()

        val = item.get()
        print(val)

    return NoneObj()


@makeFunc("exit")
def aiLangBuiltinExit(*items):
    ret_code = None
    if len(items) > 0:
        first = items[0]
        if isinstance(first.get(), NumType) and first.get().type == NumTypes.INT:
            ret_code = first.get().get()

    ret_code = ret_code if ret_code else 0
    sys.exit(ret_code)


@makeMethod("rest", type(None))
def aiLangBuiltinDFRest(parent, *args) -> AiLangObj:  # pylint: disable=unused-argument
    return AiLangObj("")


#-----------------------------
# Logistic Regression
#-----------------------------
@makeFunc("fit_logistic_regression")
def aiLangFitLogisticRegression(
    X,
    y,
    penalty="l2",
    C=1.0,
    max_iter=100,
    multi_class="auto",
    solver="lbfgs"
):

    # unwrap all parameters
    X = unwrap(X)
    y = unwrap(y)
    penalty = unwrap(penalty)
    C = unwrap(C)
    max_iter = unwrap(max_iter)
    multi_class = unwrap(multi_class)
    solver = unwrap(solver)


    # create model
    model = LogisticRegression(
        penalty=penalty,
        C=C,
        max_iter=max_iter,
        multi_class=multi_class,
        solver=solver
    )

    # train model
    model.fit(X, y)

    # return dictionary-like result
    return AiLangObj(
        "result",
        AiLangType({
            "model": model,
            "coef_": model.coef_.tolist(),
            "intercept_": model.intercept_.tolist()
        })
    )

@makeFunc("predict_logistic")
def aiLangPredictLogistic(model, X):

    # unwrap parameters
    model = unwrap(model)
    X = unwrap(X)

    # make predictions
    y_pred = model.predict(X)
    y_proba = model.predict_proba(X)

    # return result
    return AiLangObj(
        "result",
        AiLangType({
            "y_pred": y_pred.tolist(),
            "y_proba": y_proba.tolist()
        })
    )

#-----------------------------
# Linear Regression
#-----------------------------


@makeFunc("fit_linear_regression")
def aiLangFitLinearRegression(
    X,
    y,
    fit_intercept=True,
    regularization="none",
    alpha=1.0,
    l1_ratio=0.5,
) -> AiLangObj:

    # unwrap parameters
    X = unwrap(X)
    y = unwrap(y)
    fit_intercept = unwrap(fit_intercept)
    regularization = unwrap(regularization)
    alpha = unwrap(alpha)
    l1_ratio = unwrap(l1_ratio)

    reg = regularization.lower() if isinstance(regularization, str) else "none"

    if reg == "ridge":
        model = Ridge(alpha=alpha, fit_intercept=fit_intercept)
    elif reg == "lasso":
        model = Lasso(alpha=alpha, fit_intercept=fit_intercept)
    elif reg == "elasticnet":
        model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, fit_intercept=fit_intercept)
    else:
        model = LinearRegression(fit_intercept=fit_intercept)
 
    model.fit(X, y)
    
    return _wrap({
        "model":      model,
        "coef_":      _to_list(model.coef_),
        "intercept_": float(model.intercept_) if np.ndim(model.intercept_) == 0 else _to_list(model.intercept_),
        "r2_score":   float(model.score(X, y)),
    })


@makeFunc("predict_linear")
def aiLangPredictLinear(model_result, X) -> AiLangObj:

    model_result = unwrap(model_result)
    X            = unwrap(X)
 
    model  = model_result["model"]
    y_pred = model.predict(X)
 
    return _wrap({
        "y_pred": _to_list(y_pred),
    })


#-----------------------------
# Support Vector Classifier (SVC)
#-----------------------------
@makeFunc("fit_svc")
def aiLangFitSVC(
    X,
    y,
    kernel="rbf",
    C=1.0,
    gamma="scale",
    degree=3,
    probability=False,
) -> AiLangObj:
    X           = unwrap(X)
    y           = unwrap(y)
    kernel      = unwrap(kernel)
    C           = unwrap(C)
    gamma       = unwrap(gamma)
    degree      = unwrap(degree)
    probability = unwrap(probability)
 
    model = SVC(
        kernel=kernel,
        C=C,
        gamma=gamma,
        degree=degree,
        probability=probability,
    )
    model.fit(X, y)
 
    return _wrap({
        "model":            model,
        "support_vectors_": _to_list(model.support_vectors_),
        "n_support_":       _to_list(model.n_support_),
    })
 
@makeFunc("predict_svc")
def aiLangPredictSVC(model_result, X) -> AiLangObj:
    
    model_result = unwrap(model_result)
    X            = unwrap(X)
 
    model           = model_result["model"]
    y_pred          = model.predict(X)
    decision_scores = model.decision_function(X)
 
    return _wrap({
        "y_pred":          _to_list(y_pred),
        "decision_scores": _to_list(decision_scores),
    })
#-----------------------------
# Support Vector Regressor (SVR)
#-----------------------------
@makeFunc("fit_svr")
def aiLangFitSVR(
    X,
    y,
    kernel="rbf",
    C=1.0,
    epsilon=0.1,
    gamma="scale",
) -> AiLangObj:
    
    X       = unwrap(X)
    y       = unwrap(y)
    kernel  = unwrap(kernel)
    C       = unwrap(C)
    epsilon = unwrap(epsilon)
    gamma   = unwrap(gamma)
 
    model = SVR(kernel=kernel, C=C, epsilon=epsilon, gamma=gamma)
    model.fit(X, y)
 
    return _wrap({
        "model":            model,
        "support_vectors_": _to_list(model.support_vectors_),
    })
 

@makeFunc("predict_svr")
def aiLangPredictSVR(model_result, X) -> AiLangObj:
    """
    Generate predictions from a fitted SVR model.
 
    Parameters
    ----------
    model_result : result dict returned by fit_svr
    X            : DataFrame – feature matrix
 
    Returns
    -------
    result : dict
        y_pred – list[float] predicted continuous values
    """
    model_result = unwrap(model_result)
    X            = unwrap(X)
 
    model  = model_result["model"]
    y_pred = model.predict(X)
 
    return _wrap({
        "y_pred": _to_list(y_pred),
    })
 
#-----------------------------
# Random Forest
#-----------------------------
@makeFunc("fit_random_forest")
def aiLangFitRandomForest(
    X,
    y,
    task="classification",
    n_estimators=100,
    max_depth=None,
    max_features="sqrt",
    min_samples_split=2,
    min_samples_leaf=1,
    bootstrap=True,
    random_state=None,
    n_jobs=-1,
) -> AiLangObj:

    X                 = unwrap(X)
    y                 = unwrap(y)
    task              = unwrap(task)
    n_estimators      = unwrap(n_estimators)
    max_depth         = unwrap(max_depth)
    max_features      = unwrap(max_features)
    min_samples_split = unwrap(min_samples_split)
    min_samples_leaf  = unwrap(min_samples_leaf)
    bootstrap         = unwrap(bootstrap)
    random_state      = unwrap(random_state)
    n_jobs            = unwrap(n_jobs)
 
    shared_kwargs = dict(
        n_estimators=n_estimators,
        max_depth=max_depth,
        max_features=max_features,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        bootstrap=bootstrap,
        oob_score=bootstrap,       # enables oob_score when bootstrap is True
        random_state=random_state,
        n_jobs=n_jobs,
    )
 
    if task == "regression":
        model = RandomForestRegressor(**shared_kwargs)
    else:
        model = RandomForestClassifier(**shared_kwargs)
 
    model.fit(X, y)
 
    oob = float(model.oob_score_) if bootstrap else None
 
    return _wrap({
        "model":                model,
        "feature_importances_": _to_list(model.feature_importances_),
        "oob_score_":           oob,
    })


@makeFunc("predict_random_forest")
def aiLangPredictRandomForest(model_result, X) -> AiLangObj:

    model_result = unwrap(model_result)
    X            = unwrap(X)
 
    model  = model_result["model"]
    y_pred = model.predict(X)
 
    y_proba = []
    if hasattr(model, "predict_proba"):
        y_proba = _to_list(model.predict_proba(X))
 
    return _wrap({
        "y_pred":  _to_list(y_pred),
        "y_proba": y_proba,
    })
 
 
@makeFunc("get_feature_importance_rf")
def aiLangGetFeatureImportanceRF(
    model_result,
    feature_names=None,
    top_n=None,
) -> AiLangObj:

    model_result  = unwrap(model_result)
    feature_names = unwrap(feature_names)
    top_n         = unwrap(top_n)
 
    model        = model_result["model"]
    importances  = model.feature_importances_
    n_features   = len(importances)
 
    if feature_names is None:
        feature_names = [f"feature_{i}" for i in range(n_features)]
 
    paired = sorted(
        zip(feature_names, importances.tolist()),
        key=lambda x: x[1],
        reverse=True,
    )
 
    if top_n is not None:
        paired = paired[:int(top_n)]
 
    importance_df = [{"feature": f, "importance": round(v, 6)} for f, v in paired]
 
    return _wrap({
        "importance_df": importance_df,
    })
 
#-----------------------------
# CatBoost
#-----------------------------
@makeFunc("fit_catboost")
def aiLangFitCatBoost(
    X,
    y,
    task="classification",
    cat_features=None,
    iterations=1000,
    learning_rate=None,
    depth=6,
    l2_leaf_reg=3.0,
    loss_function=None,
    eval_set=None,
    early_stopping_rounds=50,
    random_seed=42,
    task_type="CPU",
    verbose=0,
) -> AiLangObj:
    
    X                     = unwrap(X)
    y                     = unwrap(y)
    task                  = unwrap(task)
    cat_features          = unwrap(cat_features)
    iterations            = unwrap(iterations)
    learning_rate         = unwrap(learning_rate)
    depth                 = unwrap(depth)
    l2_leaf_reg           = unwrap(l2_leaf_reg)
    loss_function         = unwrap(loss_function)
    eval_set              = unwrap(eval_set)
    early_stopping_rounds = unwrap(early_stopping_rounds)
    random_seed           = unwrap(random_seed)
    task_type             = unwrap(task_type)
    verbose               = unwrap(verbose)
 
    shared_kwargs = dict(
        iterations=iterations,
        depth=depth,
        l2_leaf_reg=l2_leaf_reg,
        random_seed=random_seed,
        task_type=task_type,
        verbose=verbose,
    )
 
    # Only pass optional params when explicitly provided (CatBoost dislikes None)
    if learning_rate is not None:
        shared_kwargs["learning_rate"] = learning_rate
    if loss_function is not None:
        shared_kwargs["loss_function"] = loss_function
    if cat_features is not None:
        shared_kwargs["cat_features"] = cat_features
    if early_stopping_rounds is not None:
        shared_kwargs["early_stopping_rounds"] = early_stopping_rounds
 
    if task == "regression":
        model = CatBoostRegressor(**shared_kwargs)
    else:
        model = CatBoostClassifier(**shared_kwargs)
 
    fit_kwargs = {}
    if eval_set is not None:
        fit_kwargs["eval_set"] = eval_set
 
    model.fit(X, y, **fit_kwargs)
 
    return _wrap({
        "model":                model,
        "best_iteration_":      model.best_iteration_,
        "best_score_":          dict(model.best_score_) if model.best_score_ else {},
        "feature_importances_": _to_list(model.feature_importances_),
    })
 
 
@makeFunc("predict_catboost")
def aiLangPredictCatBoost(
    model_result,
    X,
    prediction_type="Class",
) -> AiLangObj:

    model_result    = unwrap(model_result)
    X               = unwrap(X)
    prediction_type = unwrap(prediction_type)
 
    model  = model_result["model"]
    y_pred = model.predict(X)
 
    y_proba = []
    if isinstance(model, CatBoostClassifier):
        y_proba = _to_list(model.predict_proba(X))
 
    return _wrap({
        "y_pred":  _to_list(y_pred),
        "y_proba": y_proba,
    })
 
 
@makeFunc("get_feature_importance_catboost")
def aiLangGetFeatureImportanceCatBoost(
    model_result,
    importance_type="PredictionValuesChange",
    X=None,
) -> AiLangObj:
    
    model_result    = unwrap(model_result)
    importance_type = unwrap(importance_type)
    X               = unwrap(X)
 
    model = model_result["model"]
 
    if importance_type == "ShapValues" and X is not None:
        shap_values   = _to_list(model.get_feature_importance(data=X, type="ShapValues"))
        importances   = np.abs(np.array(shap_values)[:, :-1]).mean(axis=0).tolist()
    else:
        shap_values   = []
        importances   = _to_list(model.get_feature_importance(type=importance_type))
 
    feature_names = model.feature_names_
 
    paired = sorted(
        zip(feature_names, importances),
        key=lambda x: x[1],
        reverse=True,
    )
 
    importance_df = [{"feature": f, "importance": round(v, 6)} for f, v in paired]
 
    return _wrap({
        "importance_df": importance_df,
        "shap_values":   shap_values,
    })
#-----------------------------
# K-Nearest Neighbors
#-----------------------------

@makeFunc("fit_knn")
def aiLangFitKNN(
    X,
    y,
    task="classification",
    n_neighbors=5,
    weights="uniform",
    metric="euclidean",
    algorithm="auto",
    p=2,
    n_jobs=-1,
) -> AiLangObj:

    X           = unwrap(X)
    y           = unwrap(y)
    task        = unwrap(task)
    n_neighbors = unwrap(n_neighbors)
    weights     = unwrap(weights)
    metric      = unwrap(metric)
    algorithm   = unwrap(algorithm)
    p           = unwrap(p)
    n_jobs      = unwrap(n_jobs)
 
    shared_kwargs = dict(
        n_neighbors=n_neighbors,
        weights=weights,
        metric=metric,
        algorithm=algorithm,
        p=p,
        n_jobs=n_jobs,
    )
 
    if task == "regression":
        model = KNeighborsRegressor(**shared_kwargs)
    else:
        model = KNeighborsClassifier(**shared_kwargs)
 
    model.fit(X, y)
 
    return _wrap({
        "model": model,
    })
 
 
@makeFunc("predict_knn")
def aiLangPredictKNN(model_result, X) -> AiLangObj:

    model_result = unwrap(model_result)
    X            = unwrap(X)
 
    model  = model_result["model"]
    y_pred = model.predict(X)
 
    y_proba = []
    if hasattr(model, "predict_proba"):
        y_proba = _to_list(model.predict_proba(X))
 
    distances, indices = model.kneighbors(X)
 
    return _wrap({
        "y_pred":             _to_list(y_pred),
        "y_proba":            y_proba,
        "neighbor_indices":   _to_list(indices),
        "neighbor_distances": _to_list(distances),
    })
 
 
@makeFunc("find_optimal_k")
def aiLangFindOptimalK(
    X,
    y,
    k_range=None,
    cv=5,
    metric="accuracy",
) -> AiLangObj:

    X       = unwrap(X)
    y       = unwrap(y)
    k_range = unwrap(k_range)
    cv      = unwrap(cv)
    metric  = unwrap(metric)
 
    if k_range is None:
        k_range = list(range(1, 21))
 
    cv_scores = []
    best_k     = k_range[0]
    best_score = -np.inf
 
    for k in k_range:
        knn    = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, X, y, cv=cv, scoring=metric)
        mean_s = float(scores.mean())
        std_s  = float(scores.std())
 
        cv_scores.append({
            "k":          k,
            "mean_score": round(mean_s, 6),
            "std_score":  round(std_s, 6),
        })
 
        if mean_s > best_score:
            best_score = mean_s
            best_k     = k
 
    return _wrap({
        "best_k":    best_k,
        "cv_scores": cv_scores,
    })
 