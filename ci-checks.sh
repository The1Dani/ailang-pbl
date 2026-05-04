#!/usr/bin/bash

check() {
    uv sync && \
    uv run pyright --warnings "*.py" && \
    uv run pylint -- *py && \
    uv run black --check -- *.py
}

uv run black -- *.py

if check; then
    echo Pass!
else 
    echo Fail
    exit 1
fi