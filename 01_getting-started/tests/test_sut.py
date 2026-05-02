# Chapter T-01: Getting Started & AAA Pattern
# 第T-01章：はじめてのpytestとAAAパターン
# Pattern: AAA (Arrange - Act - Assert)
# Pattern: AAA（準備 - 実行 - 検証）

import pytest

# ---------------------------------------------------------------------------
# Import the module under test (System Under Test)
# テスト対象モジュールをインポートする
# ---------------------------------------------------------------------------
# Run from the repo root: pytest 02_getting-started/
# リポジトリルートから実行: pytest 02_getting-started/
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from sut import add, divide, greet  # noqa: E402


# ===========================================================================
# Step 1: Basic assertion with AAA pattern
# Step 1: AAAパターンによる基本アサーション
# ===========================================================================
class TestAdd:
    def test_add_two_positive_integers(self) -> None:
        # Arrange -------------------------------------------------------
        # TODO: define a and b
        # TODO: a と b を定義してください
        a, b = 3, 4

        # Act -----------------------------------------------------------
        # TODO: call add(a, b) and capture the result
        # TODO: add(a, b) を呼び出して結果を変数に格納してください
        result: int | float = add(a, b)

        # Assert --------------------------------------------------------
        # TODO: assert result equals expected value
        # TODO: result が期待値と等しいことをアサートしてください
        assert result == 7

    def test_add_with_zero(self) -> None:
        # Arrange / Act / Assert
        # TODO: adding zero should return the original number
        # TODO: 0 を足しても元の数と等しいことを確認してください
        result: int | float = add(5, 0)
        assert result == 5

    def test_add_floats_with_approx(self) -> None:
        # 💡 pytest.approx: use for floating-point comparisons
        # 💡 pytest.approx: 浮動小数点の比較に使う
        # Arrange / Act / Assert
        # TODO: 0.1 + 0.2 should approximately equal 0.3
        # TODO: 0.1 + 0.2 が 0.3 とほぼ等しいことを確認してください
        result: float = add(0.1, 0.2)
        assert result == pytest.approx(0.3)
        # 💡 0.1 + 0.2 == 0.3 は Python では False になる浮動小数点の罠


# ===========================================================================
# Step 2: pytest.raises — exception testing
# Step 2: pytest.raises — 例外のテスト
# ===========================================================================
class TestDivide:
    def test_divide_normal(self) -> None:
        # TODO: 10 / 2 == 5.0
        pass

    def test_divide_by_zero_raises(self) -> None:
        # 💡 pytest.raises is the idiomatic way to assert exceptions
        # 💡 pytest.raises が例外アサーションの正しい書き方
        # TODO: calling divide(x, 0) should raise ValueError
        # TODO: divide(x, 0) が ValueError を送出することを確認してください
        pass

    def test_divide_by_zero_message(self) -> None:
        # 💡 match= accepts a regex matched against the exception message
        # 💡 match= は例外メッセージに対する正規表現
        # TODO: use pytest.raises(ValueError, match=r"zero") to check the message
        # TODO: match=r"zero" を使ってエラーメッセージも確認してください
        pass


# ===========================================================================
# Step 3: String / greeting test
# Step 3: 文字列テスト
# ===========================================================================
class TestGreet:
    def test_greet_returns_greeting(self) -> None:
        # 🧠 Testing WHAT the function returns, not HOW it is implemented
        # 🧠 実装の詳細ではなく、返り値（振る舞い）をテストする
        # TODO: greet("Alice") should contain "Alice"
        pass
