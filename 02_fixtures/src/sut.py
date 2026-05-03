# Chapter T-02: Fixtures
# Ref: https://docs.pytest.org/en/stable/how-to/fixtures.html
# この章ではpytestのfixtureを学ぶ。参照ドキュメントは上記URL。

# TODO: Implement the code to be tested.
# TODO: テスト対象のコードをここに実装してください。


def add(a: int, b: int) -> int:
    # Simple addition function as a starting SUT.
    # 足し算を行うシンプルなテスト対象関数。
    return a + b


class BankAccount:
    """A minimal bank account for fixture scope exercises."""

    # fixtureのスコープ演習用のシンプルな銀行口座クラス。

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """Deposit amount and return new balance."""
        # 入金してから残高を返す。
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Withdraw amount and return new balance."""
        # 出金してから残高を返す。
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self) -> float:
        """Return current balance."""
        # 現在の残高を返す。
        return self.balance
