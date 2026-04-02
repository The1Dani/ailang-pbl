# AiLang Developer Guide

This is a Python-based language parser project using ANTLR4.

## Project Structure

```
.
├── AiLang.g4          # ANTLR4 grammar file
├── main.py            # Entry point - parses .ail files
├── build.sh           # Build script - regenerates parser and runs tests
├── run-test.sh        # Test runner - runs .ail files through parser
├── grammar/           # Generated ANTLR4 parser files (DO NOT EDIT)
│   ├── AiLangLexer.py
│   ├── AiLangParser.py
│   ├── AiLangVisitor.py
│   └── AiLangListener.py
├── test.ail           # Test input files
└── test2.ail
```

## Build Commands

### Install dependencies
```bash
uv sync
```

### Regenerate parser from grammar
```bash
uv run -- antlr4 -Dlanguage=Python3 AiLang.g4 -visitor -o grammar/
```

### Build and run all tests
```bash
bash build.sh
```

### Run tests individually
```bash
uv run main.py test.ail
uv run main.py test2.ail
```

### Run a single test file
```bash
uv run main.py <path-to-ail-file>

# Example: run test.ail
uv run main.py test.ail
```

### Generate AST graph image
```bash
# Requires system graphviz installed: sudo apt install graphviz
uv run main.py test.ail --graph ast.png
# Or using short flag
uv run main.py test.ail -g ast.png
```

## New Files

| File | Purpose |
|------|---------|
| `ast_builder.py` | Visitor that converts parse tree to semantic AST |
| `ast_visualizer.py` | Renders AST to PNG using graphviz |

## Code Style Guidelines

### General
- Python 3.14+ required
- Use `uv` for dependency management
- Dependencies defined in `pyproject.toml`

### Naming Conventions
- **Classes**: PascalCase (e.g., `AiLangLexer`, `AiLangParser`)
- **Functions/methods**: snake_case (e.g., `visitProg`, `visitChildren`)
- **Variables**: snake_case (e.g., `input_stream`, `token_stream`)
- **Constants**: UPPER_SNAKE_CASE
- **Files**: snake_case (e.g., `main.py`, `test.ail`)

### Imports
- Standard library imports first
- Third-party imports second
- Local imports last
- Use explicit imports (avoid `from x import *`)

Example:
```python
import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from grammar.AiLangLexer import AiLangLexer
from grammar.AiLangParser import AiLangParser
```

### Type Annotations
- Use type hints for function parameters and return values when beneficial
- Follow Python 3.14+ typing conventions
- Generated ANTLR files use inline type annotations (e.g., `ctx:AiLangParser.ProgContext`)

### Grammar Development
- Edit `AiLang.g4` to modify the language syntax
- Run `antlr4` command to regenerate parser files in `grammar/`
- Generated files (in `grammar/`) should NEVER be edited manually
- Parser uses visitor pattern (`-visitor` flag)

### Error Handling
- Let ANTLR handle parse errors gracefully
- Consider adding error recovery in visitor methods
- Use try/except for runtime errors in interpreter/evaluator code

### Testing
- Test files use `.ail` extension
- Compare output against `.result` files
- Current test workflow: run file through parser, verify parse tree output

### File Patterns
- **Grammar files**: `*.g4`
- **Test input**: `*.ail`
- **Expected output**: `*.result`
- **Python source**: `*.py`

### Git Ignore
The following are ignored:
- `__pycache__/`, `*.py[oc]`
- `.venv/`
- `.antlr/`
- Generated parser files in `grammar/` (committed for convenience)

### Common Tasks

#### Add a new grammar rule
1. Edit `AiLang.g4`
2. Regenerate parser: `uv run -- antlr4 -Dlanguage=Python3 AiLang.g4 -visitor -o grammar/`
3. Implement visitor method in custom visitor class
4. Test with sample `.ail` file

#### Add a new built-in function
1. Add token/rule to `AiLang.g4`
2. Regenerate parser
3. Handle in visitor's `visitFunction` or `visitFunc` method

#### Debug parse errors
- Run: `uv run main.py <file.ail>` to see parse tree
- Check ANTLR error messages in output
- Verify grammar rules match input syntax
