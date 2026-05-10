"""Protocol definitions for ML model interfaces.

This module defines Protocol classes that describe the interfaces of ML models
wrapped by AiLang. Pyright uses these protocols to validate that the code correctly
calls methods on wrapped models.
"""

# pylint: disable=invalid-name

from typing import Protocol, Any, TypeVar


class NumpyArrayLike(Protocol):
    """Protocol for numpy array-like objects."""

    def tolist(self) -> list[Any]: ...
    def __getitem__(self, key: Any) -> Any: ...
    def __iter__(self): ...  # type: ignore[type-arg]
    def __len__(self) -> int: ...
    def __sub__(self, other: Any) -> NumpyArrayLike: ...
    def __abs__(self) -> NumpyArrayLike: ...


T = TypeVar("T")


class SklearnPredictor(Protocol):
    """Protocol for sklearn models with predict method."""

    def predict(self, x: Any) -> NumpyArrayLike: ...  # pylint: disable=unused-argument


class SklearnClassifier(SklearnPredictor):
    """Protocol for sklearn classifiers."""

    def predict_proba(  # pylint: disable=invalid-name,unused-argument
        self, x: Any
    ) -> NumpyArrayLike: ...


class SklearnLinearRegressor(SklearnPredictor):
    """Protocol for sklearn linear regressors (LinearRegression, LogisticRegression, etc.)."""

    @property
    def coef_(self) -> NumpyArrayLike: ...


class SklearnSVC(SklearnPredictor):
    """Protocol for sklearn Support Vector Classifier."""

    @property
    def support_vectors_(self) -> NumpyArrayLike: ...

    def predict_proba(  # pylint: disable=invalid-name,unused-argument
        self, x: Any
    ) -> NumpyArrayLike: ...


class SklearnSVR(SklearnPredictor):
    """Protocol for sklearn Support Vector Regressor."""

    @property
    def epsilon(self) -> float: ...


class SklearnRandomForest(SklearnPredictor):
    """Protocol for sklearn Random Forest models."""

    @property
    def feature_importances_(self) -> NumpyArrayLike: ...


class SklearnKNN(SklearnPredictor):
    """Protocol for sklearn K-Nearest Neighbors models."""

    def kneighbors(  # pylint: disable=unused-argument
        self, x: Any, n_neighbors: int | None = None  # pylint: disable=unused-argument
    ) -> tuple[NumpyArrayLike, NumpyArrayLike]: ...


class CatBoostModel(SklearnPredictor):
    """Protocol for CatBoost models."""

    def get_feature_importance(  # pylint: disable=invalid-name,unused-argument
        self,
        data: Any | None = None,  # pylint: disable=unused-argument
        type: str = "PredictionValuesChange",  # pylint: disable=unused-argument,redefined-builtin
    ) -> NumpyArrayLike: ...

    @property
    def feature_names_(self) -> list[str] | None: ...


class CatBoostPool(Protocol):
    """Protocol for CatBoost Pool objects."""


ModelProtocol = (
    SklearnPredictor
    | SklearnClassifier
    | SklearnLinearRegressor
    | SklearnSVC
    | SklearnSVR
    | SklearnRandomForest
    | SklearnKNN
    | CatBoostModel
)
