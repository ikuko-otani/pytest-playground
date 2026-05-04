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


def test_divide_raises_on_zero() -> None:
    # Arrange
    a, b = 10.0, 0.0
    # Act & Assert
    with pytest.raises(ValueError):
        divide(a, b)


# TODO: Write a test using match= to check the error message
# match= を使ってエラーメッセージを正規表現で検証するテストを書く


def test_divide_raises_with_message() -> None:
    # Arrange / Act / Assert
    with pytest.raises(ValueError, match=r"Cannot divide by zero"):
        divide(5.0, 0.0)


# TODO: Write a test verifying the raised exception value directly via excinfo
# excinfo オブジェクトで例外の値を直接検証するテストを書く


def test_divide_raises_excinfo() -> None:
    # Arrange / Act / Assert
    with pytest.raises(ValueError) as excinfo:
        divide(1.0, 0.0)
    # Assert on the exception value directly
    # 例外の値を直接アサートする
    assert "zero" in str(excinfo.value)


# ---------------------------------------------------------------------------
# Section 2: unittest.mock.patch — replacing external dependencies
# セクション2：mock.patch で外部依存を差し替える
# ---------------------------------------------------------------------------

# TODO: Write a test using @patch to mock fetch_exchange_rate
# @patch デコレータで fetch_exchange_rate をモックするテストを書く


@patch("src.sut.fetch_exchange_rate", return_value=1.35)
def test_convert_with_patch_decorator(mock_rate: MagicMock) -> None:
    # Arrange: rate is mocked to 1.35
    # Act
    result: float = convert_amount(100.0, "USD")
    # Assert
    assert result == 135.0
    mock_rate.assert_called_once_with("USD")


# TODO: Write a test using `with patch(...)` context manager form
# with patch(...) コンテキスト形式でモックするテストを書く


def test_convert_with_patch_context() -> None:
    with patch("src.sut.fetch_exchange_rate", return_value=1.10) as mock_rate:
        result: float = convert_amount(200.0, "EUR")
        assert result == pytest.approx(220.0)
        mock_rate.assert_called_once_with("EUR")


# TODO: Write a test that uses side_effect to simulate an external API failure
# side_effect で外部APIの失敗をシミュレートするテストを書く


def test_convert_raises_with_api_fails() -> None:
    with patch("src.sut.fetch_exchange_rate", side_effect=ConnectionError("API down")):
        with pytest.raises(ConnectionError, match="API down"):
            convert_amount(100.0, "USD")


# excinfo の詳細検証と浮動小数点近似テストを追記する


def test_divide_result_approx() -> None:
    # pytest.approx handles floating-point imprecision
    # 浮動小数点の誤差を吸収する
    result: float = divide(1.0, 3.0)
    assert result == pytest.approx(0.3333, rel=1e-3)


def test_divide_excinfo_type() -> None:
    with pytest.raises(ValueError) as excinfo:
        divide(7.0, 0.0)
    # Verify the exact exception type (not a subclass)
    # サブクラスではなく正確な型を確認する
    assert excinfo.type is ValueError
