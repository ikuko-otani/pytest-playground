# T-03: Parametrize

## What you learn / 学習内容

| # | Topic | 日本語 |
|---|-------|--------|
| 1 | `@pytest.mark.parametrize` basic syntax | 基本構文（argnames, argvalues） |
| 2 | `pytest.param()` with `marks=` and `id=` | マーカー付き・カスタムID |
| 3 | Stacked decorators → cartesian product | スタックデコレーター → 直積展開 |
| 4 | `pytest_generate_tests` hook | 動的パラメータ化フック |

## Reference / 参照

- Official docs: <https://docs.pytest.org/en/stable/how-to/parametrize.html>
- Sprint: 73-Day Flagship Sprint — L-W3 (Day 16)

## Run commands / 実行コマンド

```bash
# From repo root
cd 03_parametrize

# Run all tests (verbose)
pytest tests/ -v

# Coverage report
pytest tests/ --cov=src --cov-report=term-missing

# Collect-only: confirm parametrized test IDs
pytest tests/ --collect-only
```

## Coverage target / カバレッジ目標

- Target: **90%+** (recorded after Step N+1)
- Actual: 100%

## Flagship connection / Flagship への応用

- `test_create_transaction` で `amount` の境界値をパラメータ化
- `pytest.param(id="EUR->JPY")` でテストIDをビジネス語彙に変換
- `pytest_generate_tests` で testcontainers の接続先を動的取得
