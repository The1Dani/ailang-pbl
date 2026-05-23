# AiLang Library Guide

This guide shows how to add built-in functions and methods to AiLang.

Primary reference: `ailang/lib/AiLangLib.py`.

## What You’re Editing

- You add library functions/methods by writing Python and registering them at import-time with decorators.
- `main.py` imports `ailang.lib.AiLangLib`, so anything registered from there is available in the interpreter.
- `PyType` is an `AiLangType` wrapper around an arbitrary Python object (commonly a trained ML model instance).

## Function Example (`makeFunc`) With Inline Concepts

This registers a global function named `cross_validate`.

- `@makeFunc("cross_validate", ["x", "y", "cv", "metric"])`:
  - first argument is the function name visible in the DSL
  - second argument is the *positional* argument names, used by `getVars(...)`
- Inside the body, `vs = getVars(args, kwargs)` returns plain Python values keyed by those names.
- Return value must be an `AiLangObj` (often a structured object with members).

```py
@makeFunc("cross_validate", ["x", "y", "cv", "metric"])
def aiLangCrossValidate(*args, **kwargs):
    vs = getVars(args, kwargs)

    model = getModelInit(args)
    scores = cross_val_score(
        model,
        vs["x"],
        vs["y"],
        cv=int(vs["cv"]),
        scoring=vs.get("metric", "accuracy"),
    )

    result = AiLangObj("result", NoneType())
    result.setMember(AiLangObj("scores", BasicListType(scores.tolist())))
    result.setMember(
        AiLangObj("mean_score", NumType(float(scores.mean()), NumTypes.FLOAT))
    )
    return result
```

If a function is truly variadic (like `print`), set `ignore_arg_count=True`.

- `func_id` is `"print"`
- `ignore_arg_count=True` disables strict arity checking
- `kwargs` are still passed as `AiLangObj` values

```py
@makeFunc("print", ignore_arg_count=True)
def aiLangBuiltinPrint(*args, **kwargs) -> AiLangObj:
    ...
    return NoneObj()
```

Defaults for kwargs are declared on the decorator. Example from `AiLangLib.py`:

```py
@makeFunc("exit", [], kwargs={"ret_code": NoneObj()})
def aiLangBuiltinExit(*args, **kwargs):
    ...
```

Here `kwargs={"ret_code": NoneObj()}` means `ret_code` is optional in the DSL; if omitted, it defaults to `None`.

Arity rule to keep in mind:

- positional arg count must match `len(arg_names)` exactly (unless `ignore_arg_count=True`)
- kwargs are part of the signature, but defaulted kwargs may be omitted

## Method Example (`makeMethod`) With Inline Concepts

Methods dispatch on the parent value type.

- `@makeMethod("fit", Union[PyType | None], ["x", "y"])` registers a `fit` method for both `PyType` and `None` parents.
- On method calls, the runtime injects the parent as a special first argument named `_parent_`.
- `getVars(args, ...)` will include `vs["_parent_"]` as the unwrapped parent value.

```py
@makeMethod("fit", Union[PyType | None], ["x", "y"])
def aiLangFit(*args):
    vs = getVars(args)
    model = getModelInit(args)
    model.fit(vs["x"], vs["y"])
    return AiLangObj("model", PyType(model))
```

If your method is registered on `PyType`, the parent is usually the underlying Python object wrapped by `PyType`.
In `AiLangLib.py`, `score` reads that parent via `vs["_parent_"]` and returns a typed number:

```py
@makeMethod("score", PyType, ["x_test", "y_test"])
def aiLangScore(*args, **kwargs):
    vs = getVars(args, kwargs)
    score_value = vs["_parent_"].score(vs["x_test"], vs["y_test"])
    return AiLangObj("score", NumType(float(score_value), NumTypes.FLOAT))
```

## Return Rules

- Always return an `AiLangObj` (or `NoneObj()`), not a raw Python value.
- Wrap Python values in the right `AiLangType` (`NumType`, `BasicListType`, `PyType`, etc.).

## Not To Do

- Do not return raw Python values.
- Do not edit generated files under `ailang/grammar/`.
