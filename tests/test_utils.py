import json
import os
import tempfile

from src.utils import load_transactions


def test_load_transactions_valid():
    transactions = [{"id": 1, "amount": "100", "currency": "RUB"}]
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as f:
        json.dump(transactions, f)
        temp_path = f.name

    assert load_transactions(temp_path) == transactions
    os.remove(temp_path)


def test_load_transactions_empty_file():
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as f:
        f.write("")
        temp_path = f.name

    assert load_transactions(temp_path) == []
    os.remove(temp_path)


def test_load_transactions_not_list():
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as f:
        json.dump({"key": "value"}, f)
        temp_path = f.name

    assert load_transactions(temp_path) == []
    os.remove(temp_path)


def test_load_transactions_file_not_found():
    assert load_transactions("nonexistent.json") == []
