# Chapter T-02: Fixtures
# Ref: https://docs.pytest.org/en/stable/how-to/fixtures.html
# Pattern: AAA (Arrange - Act - Assert)
# AAAパターン（準備 - 実行 - 検証）でテストを書く。

import pytest
from src.sut import BankAccount, add

# ---------------------------------------------------------------------------
# Step 1: Basic @pytest.fixture + yield teardown
# Step 1: 基本的な@pytest.fixtureとyieldによるteardown
# ---------------------------------------------------------------------------

# TODO: Define a fixture named `account` that creates a BankAccount("Alice", 100.0)
#       and yields it, then prints a teardown message after the test.
# TODO: fixture `account` を定義して BankAccount("Alice", 100.0) を yield し、
#       テスト後にteardownメッセージを出力してください。


# TODO: Write a test `test_deposit` that uses the `account` fixture.
#       Arrange: account fixture provides a BankAccount with balance 100.0
#       Act:     call account.deposit(50.0)
#       Assert:  balance == 150.0
# TODO: `account` fixture を使う test_deposit を書いてください。


# TODO: Write a test `test_withdraw_insufficient` that uses the `account` fixture
#       and asserts that withdrawing 200.0 raises ValueError.
# TODO: 200.0 出金で ValueError が出ることを検証するテストを書いてください。


# ---------------------------------------------------------------------------
# Step 2: Fixture scope (module) + conftest.py
# Step 2: fixtureスコープ（module）とconftest.py
# ---------------------------------------------------------------------------

# NOTE: `module_account` fixture is defined in conftest.py with scope="module".
# NOTE: `module_account` fixture は conftest.py に scope="module" で定義します。

# TODO: Write two tests that BOTH request `module_account`.
#       Verify that both tests receive the SAME object (shared instance).
# TODO: 両テストが同一オブジェクトを受け取ることを確認する2つのテストを書いてください。


# ---------------------------------------------------------------------------
# Step 3: autouse + Factory as Fixture
# Step 3: autouse と Factory as Fixture
# ---------------------------------------------------------------------------

# TODO: Define a fixture `make_account` that returns a factory function:
#       def _factory(owner: str, balance: float = 0.0) -> BankAccount
# TODO: `make_account` fixture で BankAccount を生成するファクトリ関数を返してください。


# TODO: Write tests using `make_account` to create accounts with different balances.
# TODO: `make_account` を使って異なる残高の口座を作るテストを書いてください。


# ---------------------------------------------------------------------------
# Step 4: Parametrized fixture
# Step 4: パラメータ化 fixture
# ---------------------------------------------------------------------------

# TODO: Define a fixture `deposit_amount` parametrized with [10.0, 50.0, 100.0].
# TODO: [10.0, 50.0, 100.0] でパラメータ化された fixture `deposit_amount` を定義してください。


# TODO: Write a test that uses both `account` and `deposit_amount`.
#       Assert that after deposit, balance > 100.0.
# TODO: `account` と `deposit_amount` を使い、入金後の残高が 100.0 超であることを確認してください。
