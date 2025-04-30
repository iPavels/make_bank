import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    assert all(tx["operationAmount"]["currency"]["code"] == "USD" for tx in result)


def test_filter_by_currency_rub(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_by_currency_empty():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_filter_by_currency_none_found(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert result == []


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Перевод организации", "Оплата", "Перевод с карты на карту"]


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


def test_transaction_descriptions_partial_missing():
    txs = [{"description": "Описание есть"}, {"no_description": True}]
    result = list(transaction_descriptions(txs))
    assert result == ["Описание есть"]



@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_format():
    result = next(card_number_generator(42, 42))
    assert result == "0000 0000 0000 0042"
