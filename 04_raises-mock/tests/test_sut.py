# Chapter T-04: pytest.raises / unittest.mock.patch
# 第T-04章：pytest.raises / unittest.mock.patch
# Pattern: AAA (Arrange - Act - Assert)
# パターン：AAA（準備 - 実行 - 検証）

import pytest
from unittest.mock import patch, MagicMock

# Import the module under test
# テスト対象モジュールのインポート
from src.sut import divide, convert_amount

# ---------------------------------------------------------------------------
# Section 1: pytest.raises — basic exception testing
# セクション1：pytest.raises による例外テスト
# ---------------------------------------------------------------------------

# TODO: Write a test that verifies divide() raises ValueError when b=0
# b=0 のとき ValueError が送出されることを検証するテストを書く
# ✍️ YOUR CODE HERE


# TODO: Write a test using match= to check the error message
# match= を使ってエラーメッセージを正規表現で検証するテストを書く
# ✍️ YOUR CODE HERE


# TODO: Write a test verifying the raised exception value directly via excinfo
# excinfo オブジェクトで例外の値を直接検証するテストを書く
# ✍️ YOUR CODE HERE


# ---------------------------------------------------------------------------
# Section 2: unittest.mock.patch — replacing external dependencies
# セクション2：mock.patch で外部依存を差し替える
# ---------------------------------------------------------------------------

# TODO: Write a test using @patch to mock fetch_exchange_rate
# @patch デコレータで fetch_exchange_rate をモックするテストを書く
# ✍️ YOUR CODE HERE


# TODO: Write a test using `with patch(...)` context manager form
# with patch(...) コンテキスト形式でモックするテストを書く
# ✍️ YOUR CODE HERE


# TODO: Write a test that uses side_effect to simulate an external API failure
# side_effect で外部APIの失敗をシミュレートするテストを書く
# ✍️ YOUR CODE HERE
