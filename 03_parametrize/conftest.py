# Chapter T-03: Parametrize — conftest.py
# 第3章 パラメータ化 — conftest.py
# Used for: pytest_generate_tests hook (Step 4)
# 用途：pytest_generate_tests フック（ステップ4）

import pytest


# ---------------------------------------------------------------------------
# pytest_generate_tests hook
# Dynamically parametrize test functions based on their argnames.
# argnames をもとに動的にパラメータ化するフック
# ---------------------------------------------------------------------------
# ✍️  Implement pytest_generate_tests here in Step 4
# ステップ4でここに実装する
def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    # TODO: implement dynamic parametrization
    # Dynamically parametrize 'currency_code' fixture if requested
    # テストが 'currency_code' 引数を要求したら動的にパラメータ化する
    if "currency_code" in metafunc.fixturenames:
        metafunc.parametrize(
            "currency_code",
            [
                "USD",
                "EUR",
                "JPY",
            ],
            ids=lambda c: c,
        )
