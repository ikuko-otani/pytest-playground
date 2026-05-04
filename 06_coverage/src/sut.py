# Chapter T-06: Coverage (pytest-cov)
# 日本語訳：第6章 - カバレッジ（pytest-cov）
# Ref: https://pytest-cov.readthedocs.io/en/latest/readme.html

# TODO: Implement the code to be tested.
# TODO: テスト対象のコードを実装してください。


def add(a: int, b: int) -> int:
    # Returns the sum of a and b.
    # 日本語訳：a と b の合計を返す。
    return a + b


def divide(a: float, b: float) -> float:
    # Returns a divided by b. Raises ValueError if b is zero.
    # 日本語訳：a を b で割った値を返す。b がゼロのときは ValueError を送出する。
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def classify_score(score: int) -> str:
    # Classifies a score into 'excellent', 'pass', or 'fail'.
    # 日本語訳：スコアを 'excellent', 'pass', 'fail' に分類する。
    # This function has multiple branches — great for branch coverage practice.
    # 日本語訳：複数の分岐を持つ関数 — ブランチカバレッジの練習に最適。
    if score >= 90:
        return "excellent"
    elif score >= 60:
        return "pass"
    else:
        return "fail"


def is_even(n: int) -> bool:
    # Returns True if n is even, False otherwise.
    # 日本語訳：n が偶数なら True、そうでなければ False を返す。
    return n % 2 == 0


def unreachable_function() -> str:  # pragma: no cover
    # This function is intentionally excluded from coverage.
    # 日本語訳：この関数はカバレッジ計測から意図的に除外されている。
    # Used to demonstrate '# pragma: no cover' directive.
    # 日本語訳：'# pragma: no cover' ディレクティブのデモ用。
    return "I will never be tested"
