# Chapter T-04: pytest.raises / unittest.mock.patch
# 第T-04章：pytest.raises / unittest.mock.patch
# Ref: https://docs.pytest.org/en/stable/how-to/assert.html
# 参考ドキュメント

# TODO: Implement the code to be tested.
# テスト対象のコードをここに実装してください。


import httpx  # simulating an external call


def divide(a: float, b: float) -> float:
    """Divide a by b. Raises ValueError if b is zero."""
    # a を b で割る。b がゼロなら ValueError を送出する。
    # TODO: implement
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def fetch_exchange_rate(currency: str) -> float:
    """Fetch exchange rate from external API (real implementation)."""
    # 外部APIから為替レートを取得する（テストではモックで差し替える）。
    # TODO: implement (will be patched in tests)
    # Real implementation would call an HTTP API
    response = httpx.get(f"https://api.exchangerate.example/{currency}")
    return response.json()["rate"]


def convert_amount(amount: float, currency: str) -> float:
    """Convert amount using fetch_exchange_rate."""
    # fetch_exchange_rate を使って金額を変換する。
    # TODO: implement
    rate = fetch_exchange_rate(currency)
    return amount * rate
