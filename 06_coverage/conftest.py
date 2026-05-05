# conftest.py for Chapter T-06: Coverage (pytest-cov)
# 第6章 カバレッジ用 conftest.py
#
# This file is intentionally minimal for this chapter.
# この章ではシンプルな構成にしている。
# Fixtures for DB/async patterns are covered in T-03 to T-05.
# DB / 非同期パターンの fixture は T-03〜T-05 でカバー済み。
#
# You may add shared fixtures here if needed during the exercise.
# 演習中に共有 fixture が必要になった場合はここに追加してください。

import pytest


@pytest.fixture
def sample_scores() -> list[int]:
    # Returns a list of scores covering all branches of classify_score().
    # classify_score() の全分岐をカバーするスコアのリストを返す。
    return [95, 75, 40]
