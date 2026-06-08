"""Tests for the validation feature (Block2Validate / @Validate)."""

import io
import pytest

import ailang.lib.AiLangLib as _

from ailang.engine.AiLangFunc import FunctionSpace, MethodSpace
from ailang.engine.AiLangObj import AiLangObj
from ailang.engine.AiLangType import BasicListType, MapType, NumType, NumTypes

from main import runAilang


def test_no_validate_blocks_still_works():
    """Pipeline without @Validate blocks runs normally."""
    code = """
    function nop <- (x) {
        return x
    }

    -> @Start {}
    @Start -> { .print <- ("ok") }
    """
    # Should not raise
    runAilang(code)


def test_validate_missing_function_raises():
    """@Validate referencing a function that is not defined raises before execution."""
    code = """
    -> @Start {}
    @Start -> { model := 42 } -> @Nope(model)
    """
    with pytest.raises(ValueError, match="not defined"):
        runAilang(code)


def test_validate_missing_validate_select_raises():
    """When @Validate blocks exist, validate_select must be defined."""
    code = """
    function validate <- (model) {
        return model
    }
    -> @Start {}
    @Start -> { model := 42 } -> @Validate(model)
    """
    with pytest.raises(ValueError, match="validate_select"):
        runAilang(code)


def test_validate_accumulates_scores():
    """Multiple @Validate branches accumulate scores and call validate_select."""
    output = io.StringIO()
    code = f"""
    function validate <- (model) {{
        return model
    }}

    function validate_select <- (scores_map) {{
        _print <- ("scores:", scores_map.scores)
        _print <- ("models:", scores_map.models)
    }}

    -> @Start {{}}
    @Start -> {{ model := 10 }} -> @Validate(model)
    @Start -> {{ model := 20 }} -> @Validate(model)
    """

    import ailang.lib.AiLangLib as _
    from ailang.engine.Interpreter import Interpreter
    from antlr4 import InputStream, CommonTokenStream
    from ailang.grammar.AiLangLexer import AiLangLexer
    from ailang.grammar.AiLangParser import AiLangParser

    input_stream = InputStream(code)
    lexer = AiLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = AiLangParser(token_stream)
    tree = parser.prog()
    interp = Interpreter(tree)
    interp.interp()

    assert len(interp.validate_results) == 2
    scores = [r[0] for r in interp.validate_results]
    assert scores == [10, 20]


def test_map_type_has_scores_and_models_members():
    """MapType stores (score, model) pairs with .scores and .models accessors."""
    model_a = AiLangObj("model_a", NumType(10, NumTypes.INT))
    model_b = AiLangObj("model_b", NumType(20, NumTypes.INT))
    pairs = [(10, model_a), (20, model_b)]

    mt = MapType(pairs)
    assert mt.getScores() == [10, 20]

    assert mt.getModels() == [model_a, model_b]


def test_select_best_returns_highest_score_model():
    """select_best returns the model with the highest score."""
    scores = AiLangObj("scores", BasicListType([10, 20]))
    models = AiLangObj("models", BasicListType([10, 20]))

    result = FunctionSpace().call("select_best", [scores, models], {})
    assert result is not None
    assert result.get().get() == 20


def test_select_best_with_negative_scores():
    """select_best handles negative scores correctly."""
    scores = AiLangObj("scores", BasicListType([-5, -1, -10]))
    models = AiLangObj("models", BasicListType([-5, -1, -10]))

    result = FunctionSpace().call("select_best", [scores, models], {})
    assert result is not None
    assert result.get().get() == -1


def test_select_best_single_model():
    """select_best works with a single model."""
    scores = AiLangObj("scores", BasicListType([42]))
    models = AiLangObj("models", BasicListType([42]))

    result = FunctionSpace().call("select_best", [scores, models], {})
    assert result is not None
    assert result.get().get() == 42


def test_select_best_ties_returns_first():
    """select_best returns the first model encountered on ties."""
    scores = AiLangObj("scores", BasicListType([10, 10]))
    models = AiLangObj("models", BasicListType([10, 20]))

    result = FunctionSpace().call("select_best", [scores, models], {})
    assert result is not None
    assert result.get().get() == 10


# --- While loop tests ---


def _run_prog_with_validate(prog: str) -> Interpreter:
    """Parse and run a program with @Validate blocks, return the Interpreter."""
    from antlr4 import InputStream, CommonTokenStream
    from ailang.grammar.AiLangLexer import AiLangLexer
    from ailang.grammar.AiLangParser import AiLangParser
    from ailang.engine.Interpreter import Interpreter

    input_stream = InputStream(prog)
    lexer = AiLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = AiLangParser(token_stream)
    tree = parser.prog()
    interp = Interpreter(tree)
    interp.interp()
    return interp


def test_while_loop_basic():
    """While loop with simple counter terminates."""
    code = """
    function validate <- (model) { return model }
    function validate_select <- (scores_map) {
        _print <- ("done")
    }
    function count_down <- (_) {
        i <- 3
        while { i > 0 } do {
            i <- i - 1
        }
        return i
    }
    -> @Start {}
    @Start -> { model := 42 } -> @Validate(model)
    """
    _run_prog_with_validate(code)
    result = FunctionSpace().call(
        "count_down", [AiLangObj("_", NumType(0, NumTypes.INT))], {}
    )
    assert result.get().get() == 0


def test_while_loop_never_enters():
    """While body skipped when condition is false initially."""
    code = """
    function validate <- (model) { return model }
    function validate_select <- (scores_map) {
        _print <- ("done")
    }
    function test_skip <- (_) {
        result <- 99
        while { False } do {
            result <- 42
        }
        return result
    }
    -> @Start {}
    @Start -> { model := 42 } -> @Validate(model)
    """
    _run_prog_with_validate(code)
    result = FunctionSpace().call(
        "test_skip", [AiLangObj("_", NumType(0, NumTypes.INT))], {}
    )
    assert result.get().get() == 99


def test_while_loop_multi_condition():
    """While with complex & condition works."""
    code = """
    function validate <- (model) { return model }
    function validate_select <- (scores_map) {
        _print <- ("done")
    }
    function test_multi <- (_) {
        i <- 0
        n <- 5
        while { i < n & i >= 0 } do {
            i <- i + 1
        }
        return i
    }
    -> @Start {}
    @Start -> { model := 42 } -> @Validate(model)
    """
    _run_prog_with_validate(code)
    result = FunctionSpace().call(
        "test_multi", [AiLangObj("_", NumType(0, NumTypes.INT))], {}
    )
    assert result.get().get() == 5


def test_while_loop_nested_do_if():
    """While with do...if...else inside the body works."""
    code = """
    function validate <- (model) { return model }
    function validate_select <- (scores_map) {
        _print <- ("done")
    }
    function test_nested <- (_) {
        i <- 0
        best <- 0
        while { i < 5 } do {
            do {
                best <- i
            } if {
                i > best
            }
            i <- i + 1
        }
        return best
    }
    -> @Start {}
    @Start -> { model := 42 } -> @Validate(model)
    """
    _run_prog_with_validate(code)
    result = FunctionSpace().call(
        "test_nested", [AiLangObj("_", NumType(0, NumTypes.INT))], {}
    )
    assert result.get().get() == 4
