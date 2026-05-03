# Chapter T-03: Parametrize
# 第3章 パラメータ化
# Ref: https://docs.pytest.org/en/stable/how-to/parametrize.html
# TODO: Implement the code to be tested.
# テスト対象のコードを実装してください


def add(a: int, b: int) -> int:
    # TODO: implement
    # 加算を実装してください
    raise NotImplementedError


def classify_amount(amount: float) -> str:
    # TODO: implement
    # 金額を分類する関数を実装してください
    # Expected: 'negative' | 'zero' | 'small' | 'large'
    # 期待値 'negative' | 'zero' | 'small' | 'large'
    raise NotImplementedError


def parse_currency_code(code: str) -> str:
    # TODO: implement
    # 通貨コードを検証・正規化する関数を実装してください
    # Expected: raise ValueError for invalid codes
    # 無効なコードは ValueError を raise する
    raise NotImplementedError
