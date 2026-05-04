# Chapter T-04: pytest.raises / unittest.mock.patch
# 日本語訳：第T-04章：pytest.raises / unittest.mock.patch
# Ref: https://docs.pytest.org/en/stable/how-to/assert.html
# 日本語訳：参考ドキュメント

# TODO: Implement the code to be tested.
# 日本語訳：テスト対象のコードをここに実装してください。


def divide(a: float, b: float) -> float:
    """Divide a by b. Raises ValueError if b is zero."""
    # 日本語訳：a を b で割る。b がゼロなら ValueError を送出する。
    # TODO: implement
    raise NotImplementedError


def fetch_exchange_rate(currency: str) -> float:
    """Fetch exchange rate from external API (real implementation)."""
    # 日本語訳：外部APIから為替レートを取得する（テストではモックで差し替える）。
    # TODO: implement (will be patched in tests)
    raise NotImplementedError


def convert_amount(amount: float, currency: str) -> float:
    """Convert amount using fetch_exchange_rate."""
    # 日本語訳：fetch_exchange_rate を使って金額を変換する。
    # TODO: implement
    raise NotImplementedError
