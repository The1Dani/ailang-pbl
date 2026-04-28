#!/usr/bin/bash

check() {
    uv sync && \
    pyright --warnings "*.py" && \
    uv run pylint -- *py && \
    uv run black --check -- *.py
}

if check; then
    echo Pass!
else 
    echo Fail
    exit 1
fi