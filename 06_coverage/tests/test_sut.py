# Chapter T-06: Coverage (pytest-cov)
# 日本語訳：第6章 - カバレッジ（pytest-cov）
# Pattern: AAA (Arrange - Act - Assert)
# 日本語訳：パターン：AAA（準備 - 実行 - 検証）

import pytest
from src.sut import add, divide, classify_score, is_even


# ---------------------------------------------------------------------------
# Step 1: Basic line coverage — add() and is_even()
# Step 1：基本的な行カバレッジ — add() と is_even()
# ---------------------------------------------------------------------------

# TODO: Write test for add()
# TODO: add() のテストを書く

# def test_add_positive_numbers() -> None:
#     # Arrange
#     # Act
#     # Assert


# TODO: Write test for is_even() — True branch and False branch
# TODO: is_even() のテストを書く — True 分岐と False 分岐


# ---------------------------------------------------------------------------
# Step 2: Branch coverage — classify_score()
# Step 2：ブランチカバレッジ — classify_score()
# ---------------------------------------------------------------------------

# TODO: Cover all 3 branches: score >= 90, score >= 60, else
# TODO: 3つの分岐をすべてカバー: score >= 90, score >= 60, else


# ---------------------------------------------------------------------------
# Step 3: Exception path coverage — divide()
# Step 3：例外パスのカバレッジ — divide()
# ---------------------------------------------------------------------------

# TODO: Test normal division and zero-division ValueError
# TODO: 通常の除算と ZeroDivisionError の両方をテストする
