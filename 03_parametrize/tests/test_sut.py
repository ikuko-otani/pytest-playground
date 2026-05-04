# Chapter T-03: Parametrize
# 第3章 パラメータ化
# Pattern: AAA (Arrange - Act - Assert)
# パターン：AAA（準備 - 実行 - 検証）

import pytest
from src.sut import add, classify_amount, parse_currency_code


# ---------------------------------------------------------------------------
# Step 1: Basic parametrize — add()
# ステップ1 基本的なパラメータ化 — add()
# ---------------------------------------------------------------------------
# ✍️  Write @pytest.mark.parametrize and test body here
# ここに @pytest.mark.parametrize とテスト本体を書く
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),  # normal case
        (0, 0, 0),  # zero boundary
        (-1, 1, 0),  # negative + positive
        (100, -50, 50),  # large values
    ],
)
def test_add(a: int, b: int, expected: int) -> None:
    # Arrange: inputs are provided via parametrize
    # 入力はパラメータ化で与えられる
    # Act
    result: int = add(a, b)
    # Assert
    assert result == expected


# ---------------------------------------------------------------------------
# Step 2: pytest.param with xfail / skip / custom id — classify_amount()
# ステップ2 pytest.param + xfail/skip/カスタムID — classify_amount()
# ---------------------------------------------------------------------------
# ✍️  Write parametrize with pytest.param here
# ここに pytest.param を使ったパラメータ化を書く


# ---------------------------------------------------------------------------
# Step 3: Stacked decorators (cartesian product) — add()
# ステップ3 スタックデコレーター（直積）— add()
# ---------------------------------------------------------------------------
# ✍️  Write stacked @pytest.mark.parametrize here
# ここにスタックデコレーターを書く


# ---------------------------------------------------------------------------
# Step 4: pytest_generate_tests hook — dynamic parametrize
# ステップ4 pytest_generate_tests フック — 動的パラメータ化
# ---------------------------------------------------------------------------
# ✍️  (in conftest.py) implement pytest_generate_tests
# （conftest.py に）pytest_generate_tests を実装する
