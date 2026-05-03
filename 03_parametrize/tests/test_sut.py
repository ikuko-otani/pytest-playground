# Chapter T-03: Parametrize
# 日本語訳：第3章 パラメータ化
# Pattern: AAA (Arrange - Act - Assert)
# 日本語訳：パターン：AAA（準備 - 実行 - 検証）

import pytest
from src.sut import add, classify_amount, parse_currency_code


# ---------------------------------------------------------------------------
# Step 1: Basic parametrize — add()
# 日本語訳：ステップ1 基本的なパラメータ化 — add()
# ---------------------------------------------------------------------------
# ✍️  Write @pytest.mark.parametrize and test body here
# 日本語訳：ここに @pytest.mark.parametrize とテスト本体を書く


# ---------------------------------------------------------------------------
# Step 2: pytest.param with xfail / skip / custom id — classify_amount()
# 日本語訳：ステップ2 pytest.param + xfail/skip/カスタムID — classify_amount()
# ---------------------------------------------------------------------------
# ✍️  Write parametrize with pytest.param here
# 日本語訳：ここに pytest.param を使ったパラメータ化を書く


# ---------------------------------------------------------------------------
# Step 3: Stacked decorators (cartesian product) — add()
# 日本語訳：ステップ3 スタックデコレーター（直積）— add()
# ---------------------------------------------------------------------------
# ✍️  Write stacked @pytest.mark.parametrize here
# 日本語訳：ここにスタックデコレーターを書く


# ---------------------------------------------------------------------------
# Step 4: pytest_generate_tests hook — dynamic parametrize
# 日本語訳：ステップ4 pytest_generate_tests フック — 動的パラメータ化
# ---------------------------------------------------------------------------
# ✍️  (in conftest.py) implement pytest_generate_tests
# 日本語訳：（conftest.py に）pytest_generate_tests を実装する
