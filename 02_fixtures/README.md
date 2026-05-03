# T-02: Fixtures

> **Learning goal**: Master `@pytest.fixture` — from basic setup/teardown to scoped,
> parametrized, and factory fixtures used in real-world FastAPI + SQLAlchemy projects.
>
> **学習目標**: `@pytest.fixture` を使いこなし、スコープ・パラメータ化・Factory パターンを
> 実際の FastAPI + SQLAlchemy プロジェクトで応用できるようにする。

## Topics Covered / 学習トピック

| # | Topic | pytest API |
|---|-------|------------|
| 1 | Basic fixture + `yield` teardown | `@pytest.fixture` |
| 2 | Fixture scope: `function` / `module` / `session` | `scope=` |
| 3 | `conftest.py` scope hierarchy | auto-discovery |
| 4 | `autouse=True` | `autouse=` |
| 5 | Factory as Fixture pattern | returns callable |
| 6 | Parametrized fixtures | `params=`, `request.param` |

## Quick Start / 実行手順

```bash
# 1. Checkout this branch
# 1. このブランチをチェックアウト
git checkout feature/pytest-02-fixtures

# 2. Move into the exercise directory
# 2. 演習ディレクトリに移動
cd 02_fixtures

# 3. Install dependencies
# 3. 依存パッケージをインストール
pip install pytest pytest-asyncio pytest-cov

# 4. Run all tests (expect failures until TODOs are filled)
# 4. 全テストを実行（TODOを埋めるまでは失敗する）
pytest -v

# 5. Run with coverage
# 5. カバレッジ付きで実行
pytest --cov=src --cov-report=term-missing -v
```

## File Structure / ファイル構成

```
02_fixtures/
├── conftest.py          # Shared fixtures (module/session scope)
├── src/
│   └── sut.py           # System Under Test: BankAccount, add()
├── tests/
│   └── test_sut.py      # Your test implementations
└── README.md
```

## Key Concepts / 重要概念

### AAA Pattern / AAAパターン
```python
def test_deposit(account):  # Arrange: fixture injects BankAccount
    new_balance = account.deposit(50.0)  # Act
    assert new_balance == 150.0          # Assert
```

### Fixture Scope Lifecycle / fixtureスコープのライフサイクル

```
function  → created & destroyed for EACH test function
class     → shared within a test class
module    → shared within a .py file
package   → shared within a directory
session   → shared for the entire test run
```

### `conftest.py` Discovery Rule / conftest.py の探索ルール

```
tests/
├── conftest.py         ← session/module scope fixtures here
└── unit/
    ├── conftest.py     ← narrower scope fixtures here (override outer)
    └── test_foo.py
```

## Coverage Target / カバレッジ目標

`src/sut.py` の全分岐（正常系・異常系）をカバーし、**90%以上** を目指す。

## Flagship Connection / payment-ledger-api との接続

この単元で学ぶ fixture パターンは `payment-ledger-api` の以下に直結します：

- `conftest.py` → `async_session` fixture（testcontainers PostgreSQL）
- `yield` teardown → 各テスト後の DB ロールバック
- Factory as Fixture → テスト用 Payment / User データ生成
- `scope="session"` → PostgreSQL コンテナ起動コストの削減
