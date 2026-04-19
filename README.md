![Status](https://img.shields.io/badge/status-active-success?style=flat-square) ![Mode](https://img.shields.io/badge/mode-minimum_viable-blue?style=flat-square) ![Focus](https://img.shields.io/badge/current_focus-backend_flagship-success?style=flat-square)

# pytest-playground

My pytest + pytest-asyncio learning playground — the testing discipline foundation for my flagship project [`payment-ledger-api`](https://github.com/ikuko-otani).

## 🎯 Why this repo exists

High test coverage with meaningful assertions (not vanity metrics) is a differentiator for Senior Backend Engineer roles. Async-aware testing with `pytest-asyncio`, fixtures, and containerized database setups is what I will practice here before applying it to the flagship's test suite (target: 85%+ coverage).

## 📅 Learning window

**2026-05-07 → 2026-05-09** (Week 3 late of the 73-day sprint). See `learning_plan_minimum_viable.md` v3 dated 2026-04-19.

## 🗂 Planned units

### pytest fundamentals
- [ ] 01 Test discovery, assertions, and first green run
- [ ] 02 Fixtures: `function` / `module` / `session` scopes
- [ ] 03 Parametrization with `@pytest.mark.parametrize`
- [ ] 04 Mocking with `monkeypatch` and `unittest.mock`

### Async testing
- [ ] 05 `pytest-asyncio` setup and `@pytest.mark.asyncio`
- [ ] 06 Testing `AsyncClient` (httpx) against a FastAPI app
- [ ] 07 Async fixtures for database sessions
- [ ] 08 `testcontainers` for ephemeral PostgreSQL

### Discipline
- [ ] 09 Coverage with `pytest-cov` + branch coverage
- [ ] 10 Red → Green → Refactor walkthrough on a small module

## 🔗 Related repositories

- [`payment-ledger-api`](https://github.com/ikuko-otani) — flagship project (target: ship by 2026-06)
- [`python-playground`](https://github.com/ikuko-otani/python-playground) — Python foundation
- [`docker-playground`](https://github.com/ikuko-otani/docker-playground) — containerization
- [`fastapi-playground`](https://github.com/ikuko-otani/fastapi-playground) — API framework
- [`sqlalchemy-playground`](https://github.com/ikuko-otani/sqlalchemy-playground) — async DB layer

## 📚 References

- [pytest docs](https://docs.pytest.org/en/stable/)
- [pytest-asyncio docs](https://pytest-asyncio.readthedocs.io/)
- [testcontainers-python](https://testcontainers-python.readthedocs.io/)
- [httpx AsyncClient](https://www.python-httpx.org/async/)
