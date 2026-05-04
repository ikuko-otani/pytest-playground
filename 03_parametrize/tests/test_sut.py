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


@pytest.mark.parametrize(
    "amount, expected",
    [
        pytest.param(-1.0, "negative", id="below_zero"),
        pytest.param(0.0, "zero", id="exact_zero"),
        pytest.param(1.0, "small", id="small_positive"),
        pytest.param(1_000_000.0, "large", id="one_million"),
        pytest.param(
            -999_999.0,
            "negative",
            marks=pytest.mark.xfail(reason="extreme negative: not yet handled"),
            id="extreme_negative_xfail",
        ),
    ],
)
def test_classify_amount(amount: float, expected: str) -> None:
    # Act
    result: str = classify_amount(amount)
    # Assert
    assert result == expected


# ---------------------------------------------------------------------------
# Step 3: Stacked decorators (cartesian product) — add()
# ステップ3 スタックデコレーター（直積）— add()
# ---------------------------------------------------------------------------
# ✍️  Write stacked @pytest.mark.parametrize here
# ここにスタックデコレーターを書く


@pytest.mark.parametrize("a", [10, 20])
@pytest.mark.parametrize("b", [0, 1, -1])
def test_add_cartesian(a: int, b: int) -> None:
    # Arrange: a x b cartesian product (2 x 3 = 6 cases)
    # a × b の直積（2×3 = 6ケース）
    # Act
    result: int = add(a, b)
    # Assert
    assert isinstance(result, int)
    assert result == a + b


# ---------------------------------------------------------------------------
# Step 4: pytest_generate_tests hook — dynamic parametrize
# ステップ4 pytest_generate_tests フック — 動的パラメータ化
# ---------------------------------------------------------------------------
# ✍️  (in conftest.py) implement pytest_generate_tests
# （conftest.py に）pytest_generate_tests を実装する
