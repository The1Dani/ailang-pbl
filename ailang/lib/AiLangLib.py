import sys
import codecs
from pathlib import Path

from typing import Any, Union, cast

import pandas as pd
import numpy as np
from numpy.typing import NDArray
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split as sk_split

import joblib

from ailang.engine.AiLangFunc import makeFunc, makeMethod
from ailang.engine.AiLangObj import AiLangObj, NoneObj
from ailang.engine.AiLangType import NumType, NumTypes, NoneType, BasicListType, PyType

from . import AiLangBuiltinDfLib as _
from . import AiLangSimpleAlgLib as _
from .Registry import MODEL_REGISTRY
from .FuncUtils import getVars


def toStringDecoded(obj: AiLangObj) -> str:
    val = obj.get().get()
    return codecs.decode(str(val), "unicode-escape")


@makeFunc("print", ignore_arg_count=True)
def aiLangBuiltinPrint(*args, **kwargs) -> AiLangObj:

    args = list(args)

    sep, end = None, None

    if "sep" in kwargs:
        sep = toStringDecoded(kwargs["sep"])
        del kwargs["sep"]

    if "end" in kwargs:
        end = toStringDecoded(kwargs["end"])
        del kwargs["end"]

    kwarg_vals = list(kwargs.values())
    args += kwarg_vals

    # print(f"DEBUG: {args}")

    values = [toStringDecoded(val) for val in args]

    print(*values, sep=sep, end=end)

    return NoneObj()


@makeFunc("exit", [], kwargs={"ret_code": NoneObj()})
def aiLangBuiltinExit(*args, **kwargs):

    vs = getVars(args, kwargs)
    ret_code = vs["ret_code"] if isinstance(vs["ret_code"], int) else 0

    ret_code = ret_code if ret_code else 0
    sys.exit(ret_code)


@makeMethod("rest", type(None))
def aiLangBuiltinDFRest(
    parent, *args, **kwargs
) -> AiLangObj:  # pylint: disable=unused-argument
    print(f"[DEBUG] {parent=} {args=} {kwargs=}")
    return AiLangObj("")


@makeFunc("breakpoint")
def aiLangInternalBreakPoint() -> AiLangObj:
    breakpoint()  # pylint: disable=forgotten-debug-statement
    return NoneObj()


@makeFunc("save_csv", ["data", "path"], kwargs={"ids": NoneObj()})
def aiLangSaveCsv(*args, **kwargs):
    vs = getVars(args, kwargs)

    data = vs["data"]
    path = Path(vs["path"]).resolve()
    ids = vs.get("ids", None)

    # normalize data
    if not isinstance(data, list):
        data = [data]

    # unwrap pandas Series-like ids
    if ids is not None and hasattr(ids, "tolist") and not isinstance(ids, list):
        ids = ids.tolist()

    if ids is None:
        raise ValueError("save_csv requires 'ids' named argument with ID values")

    if len(ids) != len(data):
        raise ValueError("Length of ids and data must match")

    path.parent.mkdir(parents=True, exist_ok=True)

    pd.DataFrame({"Id": ids, "prediction": data}).to_csv(path, index=False)

    return NoneObj()


def getModelInit(args: tuple[AiLangObj]):
    vs = getVars(args)
    parent: AiLangObj = args[0]
    # print(parent)
    if parent.val is NoneType():
        if parent.original_reference is None:
            raise ValueError()
        model_name = parent.original_reference.ident
        if model_name not in MODEL_REGISTRY:
            raise ValueError(f"Unknown model: {model_name}")
        model = MODEL_REGISTRY[model_name]()
    else:
        model = vs["_parent_"]

    return model


@makeMethod("fit", Union[PyType | None], ["x", "y"])
def aiLangFit(*args):
    vs = getVars(args)

    x = vs["x"]
    y = vs["y"]

    model = getModelInit(args)

    model.fit(x, y)

    # ---- wrap ----
    wrapped = PyType(model)
    # print(type(model))
    return AiLangObj("model", wrapped)


@makeMethod("predict", PyType, ["x"])
def aiLangPredict(*args, **kwargs):
    vs = getVars(args, kwargs)

    model = vs["_parent_"]
    x = vs["x"]

    y_pred = model.predict(x)

    return AiLangObj("y_pred", BasicListType(y_pred.tolist()))


@makeMethod("score", PyType, ["x_test", "y_test"])
def aiLangScore(*args, **kwargs):
    vs = getVars(args, kwargs)

    model = vs["_parent_"]
    x_test = vs["x_test"]
    y_test = vs["y_test"]

    score_value = model.score(x_test, y_test)

    return AiLangObj("score", NumType(float(score_value), NumTypes.FLOAT))


@makeMethod("cross_validate", Union[PyType | None], ["x", "y", "cv", "metric"])
def aiLangCrossValidate(*args, **kwargs):
    vs = getVars(args, kwargs)

    model = getModelInit(args)
    x = vs["x"]
    y = vs["y"]
    cv = int(vs["cv"])
    metric = vs.get("metric", "accuracy")

    scores = cross_val_score(model, x, y, cv=cv, scoring=metric)

    result = AiLangObj("result", NoneType())
    result.setMember(AiLangObj("scores", BasicListType(scores.tolist())))

    result.setMember(
        AiLangObj("mean_score", NumType(float(scores.mean()), NumTypes.FLOAT))
    )

    return result


@makeMethod("save_model", PyType, ["path"])
def aiLangSaveModel(*args, **kwargs):
    vs = getVars(args, kwargs)

    path = vs["path"]

    model = vs["_parent_"]

    joblib.dump(model, path)

    return NoneObj()


@makeFunc("load_model", ["path"])
def aiLangLoadModel(*args, **kwargs):
    vs = getVars(args, kwargs)

    path = vs["path"]

    model = joblib.load(path)

    wrapped = PyType(model)

    result = AiLangObj("model", wrapped)

    return result


@makeFunc("train_test_split", ["x", "y", "test_size"])
def aiLangTrainTestSplit(*args, **kwargs):
    vs = getVars(args, kwargs)

    x: Any = vs["x"]
    y: Any = vs["y"]
    test_size = float(vs["test_size"])

    x_arr = np.asarray(x)
    y_arr = np.asarray(y)
    split_result = cast(
        tuple[
            NDArray[np.float64],
            NDArray[np.float64],
            NDArray[np.float64],
            NDArray[np.float64],
        ],
        sk_split(x_arr, y_arr, test_size=test_size),
    )
    x_train, x_test, y_train, y_test = split_result

    if x_train is None or x_test is None or y_train is None or y_test is None:
        raise ValueError("train_test_split returned None values")

    result = AiLangObj("split", NoneType())

    result.setMember(
        AiLangObj("X_train", BasicListType(cast(list[float], x_train.tolist())))
    )
    result.setMember(
        AiLangObj("X_test", BasicListType(cast(list[float], x_test.tolist())))
    )
    result.setMember(
        AiLangObj("y_train", BasicListType(cast(list[float], y_train.tolist())))
    )
    result.setMember(
        AiLangObj("y_test", BasicListType(cast(list[float], y_test.tolist())))
    )

    return result
