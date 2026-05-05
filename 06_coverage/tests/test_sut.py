# Chapter T-06: Coverage (pytest-cov)
# 第6章 - カバレッジ（pytest-cov）
# Pattern: AAA (Arrange - Act - Assert)
# パターン：AAA（準備 - 実行 - 検証）

import pytest
from src.sut import add, divide, classify_score, is_even

# ---------------------------------------------------------------------------
# Step 1: Basic line coverage — add() and is_even()
# Step 1：基本的な行カバレッジ — add() と is_even()
# ---------------------------------------------------------------------------


# TODO: Write test for add()
# TODO: add() のテストを書く


def test_add_positive_numbers() -> None:
    # Arrange
    a, b = 3, 5
    # Act
    result: int = add(a, b)
    # Assert
    assert result == 8


# TODO: Write test for is_even() — True branch and False branch
# TODO: is_even() のテストを書く — True 分岐と False 分岐


def test_is_even_true() -> None:
    assert is_even(4) is True


def test_is_even_false() -> None:
    assert is_even(3) is False


# ---------------------------------------------------------------------------
# Step 2: Branch coverage — classify_score()
# Step 2：ブランチカバレッジ — classify_score()
# ---------------------------------------------------------------------------

# TODO: Cover all 3 branches: score >= 90, score >= 60, else
# TODO: 3つの分岐をすべてカバー: score >= 90, score >= 60, else


def test_classify_score_excellent() -> None:
    result: str = classify_score(95)
    assert result == "excellent"


def test_classify_score_pass() -> None:
    result: str = classify_score(75)
    assert result == "pass"


def test_classify_score_fail() -> None:
    result: str = classify_score(40)
    assert result == "fail"


# ---------------------------------------------------------------------------
# Step 3: Exception path coverage — divide()
# Step 3：例外パスのカバレッジ — divide()
# ---------------------------------------------------------------------------

# TODO: Test normal division and zero-division ValueError
# TODO: 通常の除算と ZeroDivisionError の両方をテストする
