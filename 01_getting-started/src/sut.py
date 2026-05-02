# Chapter T-01: Getting Started & AAA Pattern
# 第T-01章：はじめてのpytestとAAAパターン
# Ref: https://docs.pytest.org/en/stable/getting-started.html

# TODO: Implement the functions to be tested.
# TODO: テスト対象の関数をここに実装してください。


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of two numbers."""
    # TODO: implement
    # TODO: 実装してください
    return a + b


def divide(a: float, b: float) -> float:
    """Return a divided by b. Raises ValueError if b is zero."""
    # TODO: implement, raise ValueError when b == 0
    # TODO: b が 0 のとき ValueError を送出するように実装してください
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def greet(name: str) -> str:
    """Return a greeting string for the given name."""
    # TODO: implement
    # TODO: 実装してください
    return f"Hello, {name}!"
