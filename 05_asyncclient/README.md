# T-05: pytest-asyncio (AsyncClient)

## What you'll learn / 学習内容

| Topic | Description |
|---|---|
| `@pytest.mark.asyncio` | Marks a coroutine as an async test |
| `asyncio_mode = auto` | Eliminates the need for explicit markers in `pytest.ini` |
| `@pytest_asyncio.fixture` | Defines async fixtures (replaces `@pytest.fixture` for coroutines) |
| `loop_scope` | Controls the lifetime of the event loop (function / module / session) |
| `httpx.AsyncClient` + `ASGITransport` | Tests FastAPI endpoints without spinning up a real server |
| AAA Pattern | Arrange → Act → Assert applied to async flows |
| Coverage | `pytest --cov=src --cov-report=term-missing` |

## Flagship relevance / Flagship への応用

These patterns map directly to `payment-ledger-api`:
- `async_client` fixture → test `POST /transactions`, `GET /ledger`
- `scope="module"` + `loop_scope="module"` → reuse DB session fixture across tests
- `asyncio_mode = auto` → cleaner test files project-wide

## Setup / セットアップ

```bash
# Install dependencies
pip install fastapi httpx pytest pytest-asyncio pytest-cov

# Run tests (from inside 05_asyncclient/)
cd 05_asyncclient
pytest -v

# Run with coverage
pytest --cov=src --cov-report=term-missing
```

## Directory structure / ディレクトリ構成

```
05_asyncclient/
├── conftest.py          # Shared fixtures (async_client)
├── pytest.ini           # asyncio_mode = auto
├── src/
│   └── sut.py           # FastAPI app (System Under Test)
└── tests/
    └── test_sut.py      # Test file (AAA pattern)
```

## Coverage record / カバレッジ記録

<!-- Update after Step N+1 -->
- [ ] Target: 85%+
- [ ] Actual: TBD
