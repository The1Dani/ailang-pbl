
import sys
import codecs

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split as sk_split

import joblib

from AiLangFunc import makeFunc, makeMethod
from AiLangObj import AiLangObj, NoneObj, ModelType
from AiLangType import NumType, NumTypes, NoneType, BasicListType
import AiLangBuiltinDfLib as _
import AiLangSimpleAlgLib as _

from Registry import MODEL_REGISTRY

def unwrap(value):
    if isinstance(value, AiLangObj):
        value = value.get()
    if hasattr(value, "get"):
        value = value.get()
    return value


def toStringDecoded(obj: AiLangObj) -> str:
    val = obj.get().get()
    return codecs.decode(str(val), "unicode-escape")


@makeFunc("print")
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

    print(f"DEBUG: {args}")

    values = [toStringDecoded(val) for val in args]

    print(*values, sep=sep, end=end)

    return NoneObj()


@makeFunc("exit")
def aiLangBuiltinExit(*items: AiLangObj):
    ret_code = None
    if len(items) > 0:
        first = items[0]
        first_type = first.get()
        if isinstance(first_type, NumType):
            if first_type.type == NumTypes.INT:
                ret_code = first_type.get()

    ret_code = ret_code if ret_code else 0
    sys.exit(ret_code)


@makeMethod("rest", type(None))
def aiLangBuiltinDFRest(
    parent, *args, **kwargs
) -> AiLangObj:  # pylint: disable=unused-argument
    print(f"[DEBUG] {parent=} {args=} {kwargs=}")
    return AiLangObj("")

@makeFunc("fit")
def aiLangFit(*items):

    if len(items) < 3:
        raise ValueError()

    model_name = unwrap(items[0])
    x = unwrap(items[1])
    y = unwrap(items[2])

    params = unwrap(items[3]) if len(items) > 3 else {}

    if isinstance(model_name, str):
        model_name = model_name
    else:
        model_name = model_name.get()

    if model_name not in MODEL_REGISTRY:
        raise ValueError(f"Unknown model: {model_name}")

    model_class = MODEL_REGISTRY[model_name]

    # ---- create model dynamically ----
    model = model_class(**params)

    # ---- train ----
    model.fit(x, y)

    # ---- wrap ----
    wrapped = ModelType(model)

    result = AiLangObj("model", wrapped)

    return result

@makeFunc("predict")
def aiLangPredict(*items):

    if len(items) < 2:
        raise ValueError()

    model_obj = unwrap(items[0])
    x = unwrap(items[1])

    model = model_obj.getMember("model").get()

    y_pred = model.predict(x)

    result = AiLangObj("result", NoneType())
    result.setMember(
        AiLangObj("y_pred", BasicListType(y_pred.tolist()))
    )

    # optional probability support
    if hasattr(model, "predict_proba"):
        result.setMember(
            AiLangObj("y_proba", BasicListType(model.predict_proba(x).tolist()))
        )

    return result

@makeFunc("score")
def aiLangScore(*items):

    if len(items) < 3:
        raise ValueError()

    model_obj = unwrap(items[0])
    x_test = unwrap(items[1])
    y_test = unwrap(items[2])

    model = model_obj.getMember("model").get()

    score_value = model.score(x_test, y_test)

    result = AiLangObj("result", NoneType())
    result.setMember(
        AiLangObj("score", NumType(float(score_value), NumTypes.FLOAT))
    )

    return result


@makeFunc("cross_validate")
def aiLangCrossValidate(*items):

    if len(items) < 4:
        raise ValueError()

    model_name = unwrap(items[0])
    x = unwrap(items[1])
    y = unwrap(items[2])
    cv = int(unwrap(items[3]))
    metric = unwrap(items[4]) if len(items) > 4 else "accuracy"

    if isinstance(model_name, str):
        model_name = model_name
    else:
        model_name = model_name.get()

    if model_name not in MODEL_REGISTRY:
        raise ValueError("Unknown model")

    model_class = MODEL_REGISTRY[model_name]

    model = model_class()

    scores = cross_val_score(model, x, y, cv=cv, scoring=metric)

    result = AiLangObj("result", NoneType())
    result.setMember(
        AiLangObj(
            "scores",
            BasicListType(scores.tolist())
        )
    )

    result.setMember(
        AiLangObj(
            "mean_score",
            NumType(float(scores.mean()), NumTypes.FLOAT)
        )
    )

    return result


@makeFunc("save_model")
def aiLangSaveModel(*items):

    if len(items) < 2:
        raise ValueError()

    model_obj = unwrap(items[0])
    path = unwrap(items[1])

    model = model_obj.getMember("model").get()

    joblib.dump(model, path)

    return NoneObj()

@makeFunc("load_model")
def aiLangLoadModel(*items):

    if len(items) < 1:
        raise ValueError()

    path = unwrap(items[0])

    model = joblib.load(path)

    wrapped = ModelType(model)

    result = AiLangObj("model", wrapped)

    return result


@makeFunc("train_test_split")
def aiLangTrainTestSplit(*items):

    if len(items) < 3:
        raise ValueError()

    x = unwrap(items[0])
    y = unwrap(items[1])
    test_size = float(unwrap(items[2]))

    x_train, x_test, y_train, y_test = sk_split(
        x, y, test_size=test_size
    )

    result = AiLangObj("split", NoneType())

    result.setMember(
        AiLangObj("X_train", AiLangObj("X_train", BasicListType(x_train.tolist())))
    )

    result.setMember(
        AiLangObj("X_test", AiLangObj("X_test", BasicListType(x_test.tolist())))
    )

    result.setMember(
        AiLangObj("y_train", AiLangObj("y_train", BasicListType(y_train.tolist())))
    )

    result.setMember(
        AiLangObj("y_test", AiLangObj("y_test", BasicListType(y_test.tolist())))
    )

    return result
