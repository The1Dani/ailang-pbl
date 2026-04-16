# AiLang

AiLang is a Domain-Specific Language (DSL) designed to simplify Machine Learning workflows. It provides a clear and structured way to define data processing, model training, and evaluation steps, reducing repetitive code and making ML pipelines easier to understand.

## Overview

AiLang is intended for:
- Developers who want to streamline machine learning workflows
- Beginners who want to understand ML pipelines in a simplified way

The language abstracts common stages of a machine learning process, such as:
- Dataset preparation
- Model definition
- Training and optimization
- Evaluation

## Technologies Used

- Python
- ANTLR4 (for lexer and parser generation)

## Installation

```bash
git clone <repo-link>
cd ailang-pbl

pip install antlr4-tools
python -m pip install antlr4-python3-runtime
```
## Project Structure
```
.
├── AiLang.g4          # ANTLR4 grammar definition
├── main.py            # Entry point (parser + interpreter)
├── build.sh           # Build script (regenerates parser + runs tests)
├── run-test.sh        # Script for running test files
├── grammar/           # Generated ANTLR4 files (DO NOT EDIT)
│   ├── AiLangLexer.py
│   ├── AiLangParser.py
│   ├── AiLangVisitor.py
│   └── AiLangListener.py
├── test.ail           # Example input file
└── test2.ail
```

## Usage
### Install dependencies (alternative using uv)
```uv sync```
### Generate parser from grammar
```uv run -- antlr4 -Dlanguage=Python3 AiLang.g4 -visitor -o grammar/```
### Run all tests and build antlr
```bash build.sh```
### Run a specific file
```
uv run main.py <file.ail>

# Example
uv run main.py helloWorld.ail
```

## AST Visualization
Generate an Abstract Syntax Tree (AST) image:
```
# Requires Graphviz installed
uv run main.py test.ail -g ast.png
```
## Features
- Custom DSL for ML workflows
- ANTLR4-based lexer and parser
- Automatic parser generation
- Test execution support
- AST generation and visualization

## How It Works
* AiLang.g4 defines the grammar of the language
* ANTLR generates the lexer and parser (```grammar/``` folder)
* main.py:
  * Reads ```.ail``` files
  * Builds the parse tree
  * Interprets the structure

## Example
```uv run main.py helloWorld.ail```
Executes an AiLang program and processes it through the parser.

## Notes
* Do not manually edit files inside ```grammar/```
* Always regenerate parser after modifying ```AiLang.g4```