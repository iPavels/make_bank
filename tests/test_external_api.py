from unittest.mock import patch

from src.external_api import get_amount_in_rub


def test_get_amount_in_rub_rub():
    transaction = {"amount": 100, "currency": "RUB"}
    assert get_amount_in_rub(transaction) == 100.0


@patch("src.external_api.requests.get")
def test_get_amount_in_rub_usd(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 9200.0}

    transaction = {"amount": 100, "currency": "USD"}
    assert get_amount_in_rub(transaction) == 9200.0


@patch("src.external_api.requests.get")
def test_get_amount_in_rub_api_error(mock_get):
    mock_get.side_effect = Exception("API error")
    transaction = {"amount": 100, "currency": "USD"}
    assert get_amount_in_rub(transaction) == 0.0
