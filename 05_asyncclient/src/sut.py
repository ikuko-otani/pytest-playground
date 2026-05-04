# Chapter T-05: pytest-asyncio (AsyncClient)
# 第5章 — pytest-asyncio（AsyncClient）
# Ref: https://pytest-asyncio.readthedocs.io/en/latest/
# TODO: Implement the code to be tested.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ---------------------------------------------------------------------------
# Application
# ---------------------------------------------------------------------------

app = FastAPI(title="T-05 SUT", version="0.1.0")

# ---------------------------------------------------------------------------
# In-memory store (keeps the SUT dependency-free for this unit)
# 依存なしのインメモリストア（本単元のスコープに合わせてシンプルに保つ）
# ---------------------------------------------------------------------------

_items: dict[int, str] = {}
_next_id: int = 1


class ItemIn(BaseModel):
    name: str
    # Type hint required on fields used in assert targets
    # assert 対象の戻り値には型ヒントを付ける


class ItemOut(BaseModel):
    id: int
    name: str


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    # ヘルスチェックエンドポイント
    return {"status": "ok"}


@app.get("/items", response_model=list[ItemOut])
async def list_items() -> list[ItemOut]:
    """Return all stored items."""
    # 全アイテムを返す
    return [ItemOut(id=k, name=v) for k, v in _items.items()]


@app.post("/items", response_model=ItemOut, status_code=201)
async def create_item(payload: ItemIn) -> ItemOut:
    """Create a new item and persist it in memory."""
    # 新規アイテムを作成してインメモリに保存する
    global _next_id
    item = ItemOut(id=_next_id, name=payload.name)
    _items[_next_id] = payload.name
    _next_id += 1
    return item


@app.get("/items/{item_id}", response_model=ItemOut)
async def get_item(item_id: int) -> ItemOut:
    """Fetch a single item; raise 404 if not found."""
    # 単一アイテムを返す。存在しない場合は 404 を返す
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemOut(id=item_id, name=_items[item_id])
