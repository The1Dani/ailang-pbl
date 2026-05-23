"""
Tests for ailang/lib/Registry.py

Every entry in MODEL_REGISTRY must instantiate without raising.
"""

import pytest

import ailang.lib.AiLangLib as _

from ailang.lib.Registry import MODEL_REGISTRY


@pytest.mark.parametrize("model_name", list(MODEL_REGISTRY.keys()))
def testRegistryInstantiates(model_name):
    """Every model key in MODEL_REGISTRY must produce an instance without error."""
    constructor = MODEL_REGISTRY[model_name]
    instance = constructor()
    assert instance is not None


def testRegistryHasExpectedKeys():
    expected = {
        "logistic_regression",
        "linear_regression",
        "ridge",
        "lasso",
        "elasticnet",
        "svc",
        "svr",
        "random_forest_classifier",
        "random_forest_regressor",
        "knn_classifier",
        "knn_regressor",
        "catboost_classifier",
        "catboost_regressor",
    }
    assert set(MODEL_REGISTRY.keys()) == expected
