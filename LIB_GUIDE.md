# AiLang Library Guide

This guide explains how to write library functions and methods using the exposed AiLang runtime files.

## What the files provide

- `AiLangType.py` defines value wrappers such as `NumType`, `StrType`, `DfType`, `BasicListType`, and `NoneType`.
- `AiLangObj.py` defines runtime objects, object members, and helpers for converting DataFrames.
- `AiLangFunc.py` provides decorators `@makeFunc` and `@makeMethod` for registering functions and methods.
- `FuncUtils.py` provides `getVars()` for extracting and unwrapping function arguments.
- `AiLangLib.py` shows how to register built-in functions and methods.
- `AiLangBuiltinDfLib.py` shows how to write DataFrame-specific methods.

## Main building blocks

### `AiLangType`

`AiLangType` is the base wrapper around raw Python values.

Common subclasses:

- `NumType(value, NumTypes.INT)` for integers
- `NumType(value, NumTypes.FLOAT)` for floats
- `StrType(value)` for strings
- `BasicListType(list_value)` for lists of basic values
- `DfType(dataframe)` for pandas DataFrames
- `NoneType()` for AiLang none

Use `.get()` to access the Python value inside a type wrapper.

### `AiLangObj`

`AiLangObj` wraps an identifier and a value.

Important methods:

- `get()` returns the wrapped value
- `set(val)` replaces the wrapped value
- `update(other)` replaces the full object state
- `setMember(member)` adds a child member
- `getMember(ident)` retrieves a child member
- `getRoot()` returns the root object

### `FuncUtils.getVars()`

Use `getVars(args, kwargs)` to extract and unwrap function arguments:

```python
from FuncUtils import getVars

def my_func(*args, **kwargs) -> AiLangObj:
    vs = getVars(args, kwargs)
    # vs is a dict with unwrapped values
    # e.g., {"name": value, "count": 5}
    name = vs.get("name")
    count = vs.get("count", 10)  # with default
    return AiLangObj("result", SomeType(...))
```

## Writing a built-in function

Use `@makeFunc("name", arg_names, kwargs, ignore_arg_count)` from `AiLangFunc`:

```python
from AiLangFunc import makeFunc
from AiLangObj import AiLangObj, NoneObj
from AiLangType import NumType, NumTypes
from FuncUtils import getVars

@makeFunc("add_one", arg_names=["value"])
def add_one(*args, **kwargs) -> AiLangObj:
    vs = getVars(args, kwargs)
    result = vs["value"] + 1
    return AiLangObj("result", NumType(result, NumTypes.INT))
```

### Decorator Parameters

- `arg_names`: List of argument names for positional parameters (e.g., `["x", "y"]`)
- `kwargs`: Dict of default keyword arguments (e.g., `{"ret_code": NoneObj()}`)
- `ignore_arg_count`: Set to `True` for variadic functions (accept any number of args)

### Return values

- Return an `AiLangObj` when the result should be stored as a named runtime object.
- Return `NoneObj()` when the function has no meaningful return value.

### Example with defaults

```python
@makeFunc("exit", arg_names=[], kwargs={"ret_code": NoneObj()})
def aiLangBuiltinExit(*args, **kwargs):
    vs = getVars(args, kwargs)
    ret_code = vs.get("ret_code", 0)
    sys.exit(ret_code if isinstance(ret_code, int) else 0)
```

### Example with ignore_arg_count

```python
@makeFunc("print", ignore_arg_count=True)
def aiLangBuiltinPrint(*args, **kwargs) -> AiLangObj:
    vs = getVars(args, kwargs)
    # Handle sep, end kwargs
    print(*args, sep=vs.get("sep"), end=vs.get("end"))
    return NoneObj()
```

## Writing a built-in method

Use `@makeMethod("name", ParentType, arg_names, kwargs)` decorator:

```python
from AiLangFunc import makeMethod
from AiLangObj import AiLangObj, fromDFtoObj
from AiLangType import DfType
from FuncUtils import getVars

@makeMethod("head", DfType, arg_names=[])
def df_head(parent, *args, **kwargs) -> AiLangObj:
    df = parent.get().get()
    new_df = df.head()
    return fromDFtoObj(parent.ident, new_df)
```

### Method patterns

- The parent object is passed as the first argument automatically.
- Validate the wrapped value type before using it.
- Return a new object for non-mutating methods.
- Use `parent.update(...)` and return `parent` for in-place methods.

## DataFrame helpers

`AiLangBuiltinDfLib.py` shows the standard DataFrame pattern.

### Convert a DataFrame to an `AiLangObj`

Use `fromDFtoObj(ident, df)`.

This creates:

- one root object holding the DataFrame
- one member per column
- each column stored as an `AiLangType.DfItem`

### In-place DataFrame method

```python
@makeMethod("dropna_ip", DfType, arg_names=[])
def dfBuiltinDropnaInplace(parent, *args, **kwargs):
    df = parent.get()
    if not isinstance(df, pd.DataFrame):
        raise ValueError()
    df.dropna()
    parent.update(fromDFtoObj(parent.ident, df))
    return parent
```

### Non-in-place DataFrame method

```python
@makeMethod("dropna", DfType, arg_names=[])
def dfBuiltinDropna(parent, *args, **kwargs):
    df = parent.get()
    if not isinstance(df, pd.DataFrame):
        raise ValueError()
    new_df = df.dropna()
    return fromDFtoObj(parent.ident, new_df)
```

## Validation rules

Use strict checks before operating on values:

- `isinstance(item, AiLangObj)`
- `isinstance(item.get(), NumType)`
- `isinstance(item.get(), DfType)`
- `isinstance(df, pd.DataFrame)`

Raise `ValueError()` for invalid input.

## Recommended workflow

1. Decide whether you need a function or a method.
2. Pick the correct decorator with appropriate parameters.
3. Use `getVars(args, kwargs)` to extract and unwrap arguments.
4. Validate the type.
5. Perform the Python operation.
6. Wrap the result back into an AiLang value or return `NoneObj()`.

## Quick reference

- `AiLangType`: typed value wrapper
- `AiLangObj`: named runtime object
- `NoneObj()`: AiLang none return object
- `fromDFtoObj()`: convert pandas DataFrame to AiLang object
- `getVars(args, kwargs)`: extract and unwrap function arguments
- `@makeFunc(...)`: register a built-in function
- `@makeMethod(...)`: register a built-in method