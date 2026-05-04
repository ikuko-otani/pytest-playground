# Chapter T-05: pytest-asyncio (AsyncClient)
# 日本語訳：第5章 — pytest-asyncio（AsyncClient）
# Pattern: AAA (Arrange - Act - Assert)
# 日本語訳：AAAパターン（準備 - 実行 - 検証）

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from src.sut import app

# ---------------------------------------------------------------------------
# TODO Step 1: Write a basic @pytest.mark.asyncio test for GET /health
# 日本語訳：Step 1 — GET /health の基本的な非同期テストを書く
#
# @pytest.mark.asyncio
# async def test_health():
#     # Arrange
#     ...
#     # Act
#     ...
#     # Assert
#     ...
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# TODO Step 2: Add a module-scoped async_client fixture in conftest.py
#             and use it here to test POST /items + GET /items/{id}
# 日本語訳：Step 2 — conftest.py に module スコープの async_client fixture を追加し
#             POST /items と GET /items/{id} をテストする
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# TODO Step 3: Test the 404 error path for GET /items/{item_id}
# 日本語訳：Step 3 — 存在しない ID で GET したときの 404 パスをテストする
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# TODO Step 4: Use loop_scope="module" and share a single event loop
#             across multiple test functions
# 日本語訳：Step 4 — loop_scope="module" で複数テスト関数がイベントループを共有する
# ---------------------------------------------------------------------------
