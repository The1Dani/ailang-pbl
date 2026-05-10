import sys
import codecs

from typing import Any, Union, cast

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split as sk_split

import joblib

from AiLangFunc import makeFunc, makeMethod
from AiLangObj import AiLangObj, NoneObj
from AiLangType import NumType, NumTypes, NoneType, BasicListType, PyType
import AiLangBuiltinDfLib as _
from FuncUtils import getVars
import AiLangSimpleAlgLib as _

from Registry import MODEL_REGISTRY
from protocols import NumpyArrayLike


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


@makeFunc("cross_validate", ["x", "y", "cv", "metric"])
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

    x_train, x_test, y_train, y_test = sk_split(x, y, test_size=test_size)

    result = AiLangObj("split", NoneType())

    result.setMember(
        AiLangObj("X_train", BasicListType(cast(NumpyArrayLike, x_train).tolist()))
    )
    result.setMember(
        AiLangObj("X_test", BasicListType(cast(NumpyArrayLike, x_test).tolist()))
    )
    result.setMember(
        AiLangObj("y_train", BasicListType(cast(NumpyArrayLike, y_train).tolist()))
    )
    result.setMember(
        AiLangObj("y_test", BasicListType(cast(NumpyArrayLike, y_test).tolist()))
    )

    return result
