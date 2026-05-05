# T-06: Coverage (`pytest-cov`)

## 🎯 What you will learn / 学習目標

- Measure **line coverage** and **branch coverage** with `pytest-cov`
- Read coverage reports: `Stmts`, `Miss`, `Cover`, `Missing` columns
- Use `--cov-fail-under` to enforce a coverage gate in CI
- Configure coverage via `pyproject.toml` (`[tool.coverage.run]`)
- Exclude code with `# pragma: no cover`
- Understand **why coverage is a means, not a goal**


- `pytest-cov` を使って **行カバレッジ** と **ブランチカバレッジ** を計測する
- カバレッジレポートの `Stmts`, `Miss`, `Cover`, `Missing` 列を読む
- `--cov-fail-under` で CI のカバレッジゲートを設定する
- `pyproject.toml` でカバレッジを設定する
- `# pragma: no cover` でコードを除外する
- **カバレッジは手段であってゴールでない** ことを理解する

---

## 📁 Directory structure / ディレクトリ構成

```
06_coverage/
├── src/
│   └── sut.py          # System Under Test (code to be tested / テスト対象コード)
├── tests/
│   └── test_sut.py     # Test file (AAA pattern / AAA パターン)
├── conftest.py         # Shared fixtures
├── pyproject.toml      # Coverage configuration (add during exercise)
└── README.md
```

---

## ▶️ Run commands / 実行コマンド

```bash
# Install dependencies
pip install pytest pytest-cov

# Run tests with line coverage
pytest --cov=src --cov-report=term-missing

# Run tests with branch coverage (recommended for interview readiness)
pytest --cov=src --cov-report=term-missing --cov-branch

# Enforce coverage gate (fail if below 85%)
pytest --cov=src --cov-report=term-missing --cov-fail-under=85

# Generate HTML report (open htmlcov/index.html in browser)
pytest --cov=src --cov-report=html
```

---

## 💡 Interview tips / 面接で聞かれるポイント

- **"What is branch coverage?"** — Tests both `True` and `False` paths of every `if`.
- **"Why not aim for 100% coverage?"** — It can incentivize trivial tests; focus on meaningful cases.
- **"How do you set a coverage gate in CI?"** — `--cov-fail-under=85` or `pyproject.toml`.
- **"What is `# pragma: no cover`?"** — Excludes a line/block from measurement (use sparingly).

---

## 📊 Coverage result (fill in after exercise) / 演習後に記録

| Module | Stmts | Miss | Branch | BrPart | Cover |
|--------|-------|------|--------|--------|-------|
| `src/sut.py` | 14 | 0 | 6 | 0 | 100% |

> Coverage target for `payment-ledger-api`: **85%+**
