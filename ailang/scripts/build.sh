#!/usr/bin/env bash

script_dir=$(dirname "$0")
grammar=$(realpath "$script_dir/../../AiLang.g4")
out=$(realpath "$script_dir/../grammar")

uv sync
uv run -- antlr4 -Dlanguage=Python3 "$grammar" -visitor -o "$out"

# "$script_dir"/run-test.sh