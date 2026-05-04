# T-04 — pytest.raises / unittest.mock.patch

## What you will learn / 学習内容

- **`pytest.raises`**: Test that your code raises the right exception with the right message.
  - `pytest.raises` — 正しい例外と正しいメッセージが送出されることをテストする。
- **`excinfo` object**: Inspect `.type`, `.value`, `.traceback` after the exception.
  - `excinfo` オブジェクト — 例外の `.type` / `.value` / `.traceback` を検査する。
- **`match=` parameter**: Validate the exception message with a regex.
  - `match=` パラメータ — 正規表現で例外メッセージを検証する。
- **`unittest.mock.patch`**: Replace external dependencies with controlled fakes.
  - `unittest.mock.patch` — 外部依存を制御可能な偽物に差し替える。
- **`side_effect`**: Simulate errors or dynamic return values.
  - `side_effect` — エラーや動的な戻り値をシミュレートする。
- **`assert_called_once_with`**: Verify a mock was called with the right arguments.
  - `assert_called_once_with` — 正しい引数でモックが呼ばれたか検証する。

## Directory structure / ディレクトリ構成

```
04_raises-mock/
├── conftest.py
├── src/
│   └── sut.py          # System Under Test — implement here
├── tests/
│   └── test_sut.py     # Write your tests here
└── README.md
```

## How to run / 実行コマンド

```bash
# Run all tests with verbose output
pytest 04_raises-mock/ -v

# Run with coverage
pytest 04_raises-mock/ --cov=04_raises-mock/src --cov-report=term-missing

# Run a specific test function
pytest 04_raises-mock/tests/test_sut.py::test_divide_raises_on_zero -v
```

## Coverage target / カバレッジ目標

<!-- Update after final run: e.g. `coverage: 92%` -->
coverage: TBD

## Berlin interview tips / ベルリン面接のポイント

- Always use `pytest.raises` as a **context manager** — never `try/except` inside tests.
- Patch **where the name is used**, not where it is defined: `patch("src.sut.fetch_exchange_rate")`.
- Avoid over-mocking: only mock what crosses a process/network boundary.
- AAA pattern: keep Arrange / Act / Assert clearly separated with blank lines.
