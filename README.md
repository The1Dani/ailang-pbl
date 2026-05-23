# AiLang

AiLang is a small domain-specific language (DSL) for machine-learning workflows. It is implemented in Python and uses ANTLR4 for parsing.

The repo currently focuses on running `.ail` programs that load data, train models (via scikit-learn), and evaluate results.

## Quick Start

### Requirements

- Python `>= 3.14` (see `pyproject.toml`)
- [`uv`](https://github.com/astral-sh/uv) for dependency management

### Install

```bash
git clone <repo-url>
cd ailang

uv sync
```

### Run

The project exposes a console script named `ailang`:

```bash
uv run ailang examples/svm.ail
```

To print the parse tree:

```bash
uv run ailang examples/svm.ail -parse
```

Sanity check (known to run in this repo):

```bash
uv run ailang test-examples/helloWorld.ail
```

Note: `examples/svm.ail` and `examples/logistic_regression.ail` currently reference `Example/*.csv` (capital `E`). In this repo the CSVs live under `examples/*.csv`, so those paths likely need updating before the examples will execute end-to-end.

## Project Layout

```text
.
├── ailang/
│   ├── engine/              # Interpreter/execution engine
│   ├── grammar/             # Generated ANTLR lexer/parser (Python)
│   ├── lib/                 # Built-in functions / libraries exposed to the DSL
│   ├── scripts/             # Helper scripts (build/test)
│   └── shared/              # Shared utilities and protocols
├── examples/                # Example AiLang programs + sample datasets
├── test-examples/           # Additional small/test programs
├── AiLang.g4                # ANTLR grammar
├── main.py                  # CLI entrypoint (wired via [project.scripts])
├── pyproject.toml           # Project config + dependencies
├── uv.lock                  # Locked dependency set for uv
└── README.md
```

## Features (Current)

- DSL syntax for describing ML workflows
- ANTLR4-based parser with a Python interpreter
- Built-in library registration (see `ailang/lib/`)
- Integrations: scikit-learn (e.g. SVM, logistic regression), CatBoost, pandas/numpy for data handling, joblib for persistence

## Examples

The `examples/` directory contains runnable programs:

- `examples/svm.ail`
- `examples/logistic_regression.ail`
- `examples/test_new.ail`

The example datasets live alongside the programs:

- `examples/train_features.csv`, `examples/train_labels.csv`
- `examples/test_features.csv`

## Notes

- The CLI entrypoint is `main.py` and is exposed as `ailang` via `[project.scripts]` in `pyproject.toml`.

## Development

Regenerate the parser from `AiLang.g4`:

```bash
./ailang/scripts/build.sh
```

Run the repo checks locally (typecheck, lint, formatting):

```bash
./ci-checks.sh
```

Generated sources live under `ailang/grammar/` and should not be edited by hand.
