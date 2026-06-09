#!/usr/bin/bash

check() {
    uv sync && \
    uv run pyright --warnings -p pyproject.toml && \
    uv run pylint . && \
    uv run black --check .
    AILANG_DATA_DIR="tests/.ailang/data" uv run pytest tests/ 
}

uv run black .

if check; then
    echo Pass!
else 
    echo Fail
    exit 1
fi
