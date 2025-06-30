import json
from typing import List, Dict


def load_transactions(filepath: str) -> List[Dict]:
    """
        Загружает список транзакций из JSON-файла.
        param filepath: путь до JSON-файла
        return: список словарей с транзакциями или пустой список
        """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []