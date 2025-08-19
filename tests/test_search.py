import pytest
from src.search import process_bank_search, process_bank_operations


@pytest.fixture
def sample_data():
    return [
        {"description": "Открытие вклада", "status": "EXECUTED", "currency": "RUB"},
        {"description": "Перевод с карты на карту", "status": "CANCELED", "currency": "USD"},
        {"description": "Оплата услуг", "status": "PENDING", "currency": "RUB"},
        {"description": "Перевод организации", "status": "EXECUTED", "currency": "EUR"},
    ]


def test_process_bank_search_found(sample_data):
    result = process_bank_search(sample_data, "вклад")
    assert len(result) == 1
    assert result[0]["description"] == "Открытие вклада"


def test_process_bank_search_case_insensitive(sample_data):
    result = process_bank_search(sample_data, "усЛУГ")
    assert len(result) == 1
    assert result[0]["description"] == "Оплата услуг"


def test_process_bank_search_not_found(sample_data):
    result = process_bank_search(sample_data, "кредит")
    assert result == []


def test_process_bank_operations_counts(sample_data):
    categories = ["вклад", "перевод", "оплата"]
    result = process_bank_operations(sample_data, categories)
    assert result["вклад"] == 1
    assert result["перевод"] == 2
    assert result["оплата"] == 1


def test_process_bank_operations_empty(sample_data):
    categories = ["кредит"]
    result = process_bank_operations(sample_data, categories)
    assert result == {}
