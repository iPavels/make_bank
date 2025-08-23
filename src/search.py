import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Возвращает список операций, где в поле description встречается search (без учета регистра).
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [op for op in data if "description" in op and pattern.search(op["description"])]


def process_bank_operations(data: list[dict], categories: list[str]) -> dict[str, int]:
    """
    Возвращает словарь {категория: количество операций}.
    """
    result = Counter()
    for op in data:
        desc = op.get("description", "").lower()
        for cat in categories:
            if cat.lower() in desc:
                result[cat] += 1
    return dict(result)
