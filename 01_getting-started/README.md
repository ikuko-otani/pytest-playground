# T-01: Getting Started & AAA Pattern

**Ref:** https://docs.pytest.org/en/stable/getting-started.html
**Branch:** `feature/pytest-01-getting-started`
**Sprint:** L-W3 / S2 (Day 14 of 73-day sprint)

## What you learn in this chapter

<!-- Learning objectives for T-01 -->
<!-- T-01の学習目標 -->

- pytest installation and test discovery rules (`test_*.py`, `*_test.py`)
  （pytest のインストールとテスト探索ルール）
- **AAA pattern** (Arrange-Act-Assert) as the universal test structure
  （AAAパターン：すべてのテストの基本構造）
- `assert` statement with pytest's introspection (human-readable failure messages)
  （assert 文と pytest による詳細な失敗メッセージ）
- `pytest.raises` for exception testing (`match=` regex included)
  （`pytest.raises` による例外テスト）
- `pytest.approx` for floating-point comparisons
  （`pytest.approx` による浮動小数点比較）
- Grouping tests with `class Test*` (each test gets a fresh instance)
  （`class Test*` によるテストのグループ化）
- `conftest.py` as the fixture sharing entry point
  （`conftest.py` — フィクスチャ共有の起点）

## Directory structure

```
01_getting-started/
├── src/
│   └── sut.py          # System Under Test (テスト対象コード)
├── tests/
│   └── test_sut.py     # Test file (テストファイル)
├── conftest.py         # Shared fixtures (共有フィクスチャ)
└── README.md
```

## How to run

```bash
# Run all tests in this chapter (from repo root)
# このチャプターの全テストを実行（リポジトリルートから）
pytest 01_getting-started/ -v

# Run with coverage
# カバレッジ付きで実行
pytest 01_getting-started/ --cov=01_getting-started/src --cov-report=term-missing -v

# Run only one class
# 1クラスだけ実行
pytest 01_getting-started/ -v -k "TestAdd"
```

## Coverage result

<!-- Update after completing all steps -->
<!-- 全ステップ完了後に記録してください -->

- Coverage: `100%`
- Missing lines: (none)

💡 「カバレッジ100%なら完璧？」→ NO。test_add_with_zero で pass のまま100%になった偽の例を思い出して。カバレッジは"実行した行"を数えるだけ。アサートの質は測れない。
