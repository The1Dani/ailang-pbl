# AiLang Library Guide

This guide explains how to write library functions and methods using the exposed AiLang runtime files.

## What the files provide

- `AiLangType.py` defines value wrappers such as `NumType`, `StrType`, `BasicListType`, `DfType`, and `NoneType`.
- `AiLangObj.py` defines runtime objects, object members, and helpers for converting DataFrames.
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

## Writing a built-in function

Use `@makeFunc("name")` from `AiLangFunc`.

Function arguments may arrive as either `AiLangObj` or `AiLangType`, so unwrap objects before using them.

Example:

```python
from AiLangFunc import makeFunc
from AiLangObj import AiLangObj, NoneObj
from AiLangType import NumType, NumTypes

@makeFunc("add_one")
def add_one(*items: AiLangObj | NumType) -> AiLangObj:

    # try not to use this
	first = items[0]
    # use this instead
    if items.len() > 0:
        first = items[0]
    else:
        raise ValueError()

	if isinstance(first, AiLangObj):
		first = first.get()

	if not isinstance(first, NumType):
		raise ValueError()

	result = first.get() + 1
	return AiLangObj("result", NumType(result, NumTypes.INT))
```

### Return values

- Return an `AiLangObj` when the result should be stored as a named runtime object.
- Return `NoneObj()` when the function has no meaningful return value.

## Writing a built-in method

Use `@makeMethod("name", ParentType, arg_types)`.

Methods receive the parent object first.

The parent type will determine if the method_name is accessable, in other words the parent must have this type to have the method in its method_space.

Example:

```python
from AiLangFunc import makeMethod
from AiLangObj import AiLangObj, fromDFtoObj
from AiLangType import DfType

@makeMethod("head", DfType, [])
def df_head(parent, *items):
	if not isinstance(parent, AiLangObj):
		raise ValueError()

	df = parent.get().get()
	new_df = df.head()
	return fromDFtoObj(parent.ident, new_df)
```

### Method patterns

- Validate `parent` is an `AiLangObj`.
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
@makeMethod("dropna_ip", DfType, [])
def dfBuiltinDropnaInplace(parent, *items):
	if not isinstance(parent, AiLangObj):
		raise ValueError()

	df = parent.get()
	if not isinstance(df, pd.DataFrame):
		raise ValueError()

	df.dropna(*items)
	parent.update(fromDFtoObj(parent.ident, df))
	return parent
```

### Non-in-place DataFrame method

```python
@makeMethod("dropna", DfType, [])
def dfBuiltinDropna(parent, *items):
	if not isinstance(parent, AiLangObj):
		raise ValueError()

	df = parent.get()
	if not isinstance(df, pd.DataFrame):
		raise ValueError()

	df.dropna(*items)
	return fromDFtoObj(parent.ident, df)
```

## Using `print` and `exit`

`AiLangLib.py` provides examples of simple built-ins.

### `print`

- Unwrap each argument if it is an `AiLangObj`.
- Print the underlying `.get()` value.
- Return `NoneObj()`.

### `exit`

- Read the first argument if provided.
- Accept integer `NumType` values for the exit code.
- Call `sys.exit(code)`.

## Validation rules

Use strict checks before operating on values:

- `isinstance(item, AiLangObj)`
- `isinstance(item.get(), NumType)`
- `isinstance(item.get(), DfType)`
- `isinstance(df, pd.DataFrame)`

Raise `ValueError()` for invalid input.

## Recommended workflow

1. Decide whether you need a function or a method.
2. Pick the correct decorator.
3. Unwrap any `AiLangObj` values.
4. Validate the type.
5. Perform the Python operation.
6. Wrap the result back into an AiLang value or return `NoneObj()`.

## Quick reference

- `AiLangType`: typed value wrapper
- `AiLangObj`: named runtime object
- `NoneObj()`: AiLang none return object
- `fromDFtoObj()`: convert pandas DataFrame to AiLang object
- `@makeFunc(...)`: register a built-in function
- `@makeMethod(...)`: register a built-in method

