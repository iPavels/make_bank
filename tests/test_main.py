import pytest

from main import filter_by_status, filter_rub, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"description": "Открытие вклада", "status": "EXECUTED", "currency": "RUB", "date": "2019-12-08"},
        {"description": "Перевод", "status": "CANCELED", "currency": "USD", "date": "2018-06-03"},
        {"description": "Оплата услуг", "status": "EXECUTED", "currency": "RUB", "date": "2018-07-18"},
    ]


def test_filter_by_status(sample_data):
    result = filter_by_status(sample_data, "EXECUTED")
    assert all(op["status"] == "EXECUTED" for op in result)
    assert len(result) == 2


def test_sort_by_date_ascending(sample_data):
    result = sort_by_date(sample_data, ascending=True)
    dates = [op["date"] for op in result]
    assert dates == sorted(dates)


def test_sort_by_date_descending(sample_data):
    result = sort_by_date(sample_data, ascending=False)
    dates = [op["date"] for op in result]
    assert dates == sorted(dates, reverse=True)


def test_filter_rub(sample_data):
    result = filter_rub(sample_data)
    assert all(op["currency"] == "RUB" for op in result)
    assert len(result) == 2
