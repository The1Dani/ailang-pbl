"""
Shared fixtures and helpers for the AiLang lib test suite.

Calling convention
------------------
All lib functions/methods are reached via FunctionSpace().call() or
MethodSpace().call(), which tags positional AiLangObj arguments with the
names declared in the @makeFunc / @makeMethod decorators before dispatching.
Builder helpers (make_*) therefore use an empty ident — it will be set by
the call mechanism.
"""

import numpy as np
import pandas as pd
import pytest
from catboost import CatBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, SVR

import ailang.lib.AiLangLib as _

from ailang.engine.AiLangFunc import FunctionSpace, MethodSpace
from ailang.engine.AiLangObj import AiLangObj
from ailang.engine.AiLangType import (
    BasicListType,
    DfType,
    NumType,
    NumTypes,
    PyType,
    StrType,
)

# ---------------------------------------------------------------------------
# Space isolation — every test sees the same full registry but any accidental
# addFunc calls inside a test are rolled back cleanly.
# ---------------------------------------------------------------------------


@pytest.fixture(autouse=True)
def restoreSpaces():
    fs_snapshot = FunctionSpace().saveSpace()
    ms_snapshot = MethodSpace().saveSpace()
    yield
    FunctionSpace().loadSpace(fs_snapshot)
    MethodSpace().loadSpace(ms_snapshot)


# ---------------------------------------------------------------------------
# AiLangObj builder helpers
# ---------------------------------------------------------------------------


def makeNum(val: float, numtype: NumTypes = NumTypes.FLOAT) -> AiLangObj:
    return AiLangObj("", NumType(val, numtype))


def makeStr(val: str) -> AiLangObj:
    return AiLangObj("", StrType(val))


def makeList(vals: list) -> AiLangObj:
    return AiLangObj("", BasicListType(vals))


def makePy(obj) -> AiLangObj:
    return AiLangObj("", PyType(obj))


def makeDf(df: pd.DataFrame) -> AiLangObj:
    return AiLangObj("", DfType(df))


# ---------------------------------------------------------------------------
# Deterministic synthetic datasets  (session-scoped — created once)
# ---------------------------------------------------------------------------

RNG = np.random.default_rng(42)


@pytest.fixture(scope="session")
def clfData():
    """40-sample, 2-feature binary classification dataset."""
    x = RNG.standard_normal((40, 2))
    y = (x[:, 0] + x[:, 1] > 0).astype(int)
    return x, y


@pytest.fixture(scope="session")
def regData():
    """40-sample, 2-feature linear regression dataset."""
    x = RNG.standard_normal((40, 2))
    y = 3 * x[:, 0] - 2 * x[:, 1] + RNG.standard_normal(40) * 0.1
    return x, y


# ---------------------------------------------------------------------------
# Pre-trained model fixtures  (session-scoped)
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def trainedClf(clfData):
    x, y = clfData
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(x, y)
    return AiLangObj("model", PyType(model))


@pytest.fixture(scope="session")
def trainedLr(regData):
    x, y = regData
    model = LinearRegression()
    model.fit(x, y)
    return AiLangObj("model", PyType(model))


@pytest.fixture(scope="session")
def trainedSvc(clfData):
    x, y = clfData
    model = SVC(kernel="linear", random_state=42)
    model.fit(x, y)
    return AiLangObj("model", PyType(model))


@pytest.fixture(scope="session")
def trainedSvr(regData):
    x, y = regData
    model = SVR(kernel="linear")
    model.fit(x, y)
    return AiLangObj("model", PyType(model))


@pytest.fixture(scope="session")
def trainedRf(clfData):
    x, y = clfData
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(x, y)
    return AiLangObj("model", PyType(model))


@pytest.fixture(scope="session")
def trainedKnn(clfData):
    x, y = clfData
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x, y)
    return AiLangObj("model", PyType(model))


@pytest.fixture(scope="session")
def trainedCatboost(clfData):
    x, y = clfData
    model = CatBoostClassifier(iterations=10, random_seed=42, verbose=0)
    model.fit(x, y)
    return AiLangObj("model", PyType(model))
