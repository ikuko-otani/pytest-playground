# Chapter T-05: pytest-asyncio (AsyncClient)
# 第5章 — pytest-asyncio（AsyncClient）
# Pattern: AAA (Arrange - Act - Assert)
# AAAパターン（準備 - 実行 - 検証）

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from src.sut import app

# ---------------------------------------------------------------------------
# TODO Step 1: Write a basic @pytest.mark.asyncio test for GET /health
# Step 1 — GET /health の基本的な非同期テストを書く
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_health_returns_ok() -> None:
    # Arrange
    transport = ASGITransport(app=app)
    # Act
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/health")
    # Assert
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# ---------------------------------------------------------------------------
# TODO Step 2: Add a module-scoped async_client fixture in conftest.py
#             and use it here to test POST /items + GET /items/{id}
# Step 2 — conftest.py に module スコープの async_client fixture を追加し
#             POST /items と GET /items/{id} をテストする
# ---------------------------------------------------------------------------

# Step 2: POST /items and GET /items/{id} using shared async_client
# 共有 async_client fixture を使って POST/GET をテストする


async def test_create_and_fetch_item(async_client: AsyncClient) -> None:
    # Arrange
    payload = {"name": "apple"}
    # Act
    created = await async_client.post("/items", json=payload)
    item_id: int = created.json()["id"]
    fetched = await async_client.get(f"/items/{item_id}")
    # Assert
    assert created.status_code == 201
    assert fetched.status_code == 200
    assert fetched.json()["name"] == "apple"


# ---------------------------------------------------------------------------
# TODO Step 3: Test the 404 error path for GET /items/{item_id}
# Step 3 — 存在しない ID で GET したときの 404 パスをテストする
# ---------------------------------------------------------------------------


async def test_get_nonexistent_item_returns_404(async_client: AsyncClient) -> None:
    # Arrange
    nonexistent_id = 99999
    # Act
    response = await async_client.get(f"/items/{nonexistent_id}")
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


# ---------------------------------------------------------------------------
# TODO Step 4: Use loop_scope="module" and share a single event loop
#             across multiple test functions
# Step 4 — loop_scope="module" で複数テスト関数がイベントループを共有する
# ---------------------------------------------------------------------------
