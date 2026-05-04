# conftest.py — T-05: pytest-asyncio (AsyncClient)
# conftest.py — 第5章の共有 fixture 置き場
#
# Fixtures defined here are available to all tests under 05_asyncclient/
# ここに定義した fixture は 05_asyncclient/ 配下の全テストで利用できる

import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from src.sut import app

# ---------------------------------------------------------------------------
# TODO: Implement an async_client fixture with appropriate scope
# 適切なスコープで async_client fixture を実装する
#
# Hint:
#   @pytest_asyncio.fixture(scope="module", loop_scope="module")
#   async def async_client() -> AsyncClient:
#       async with AsyncClient(
#           transport=ASGITransport(app=app), base_url="http://test"
#       ) as client:
#           yield client
# ---------------------------------------------------------------------------
