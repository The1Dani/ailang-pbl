# Registry.py

from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.svm import SVC, SVR
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from catboost import CatBoostClassifier, CatBoostRegressor

MODEL_REGISTRY = {
    "logistic_regression": LogisticRegression,
    "linear_regression": LinearRegression,
    "ridge": Ridge,
    "lasso": Lasso,
    "elasticnet": ElasticNet,
    "svc": SVC,
    "svr": SVR,
    "random_forest_classifier": RandomForestClassifier,
    "random_forest_regressor": RandomForestRegressor,
    "knn_classifier": KNeighborsClassifier,
    "knn_regressor": KNeighborsRegressor,
    "catboost_classifier": CatBoostClassifier,
    "catboost_regressor": CatBoostRegressor,
}