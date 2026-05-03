# conftest.py — shared fixtures for 02_fixtures chapter
# 02_fixtures章の共有fixture定義ファイル。
# Fixtures defined here are automatically available to all tests in this directory.
# ここで定義したfixtureはこのディレクトリ配下の全テストから自動で利用できる。

import pytest
from src.sut import BankAccount

# ---------------------------------------------------------------------------
# TODO: Define `module_account` fixture with scope="module".
#       Create BankAccount("Module-Shared", 500.0) and yield it.
#       Add a print statement in teardown so you can observe the lifecycle.
# ---------------------------------------------------------------------------
# TODO: scope="module" の `module_account` fixture を定義してください。
#       BankAccount("Module-Shared", 500.0) を yield し、
#       teardown時にprintでライフサイクルを確認できるようにしてください。


# ---------------------------------------------------------------------------
# 💡 Interview tip: conftest.py is NOT imported manually.
#    pytest discovers it automatically by directory hierarchy.
#    Fixtures defined closer to the test file take priority (override outer scope).
# 💡 面接ポイント: conftest.py は手動でimportしない。pytestがディレクトリ階層を
#    自動探索する。内側のconftest.pyのfixtureが外側より優先される。
# ---------------------------------------------------------------------------
