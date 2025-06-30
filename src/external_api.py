import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def get_amount_in_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли.
    param transaction: словарь с полями 'amount' и 'currency'
    return: сумма в рублях (float)
    """
    amount = float(transaction.get("amount", 0))
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return amount

    params = {
        "from": currency,
        "to": "RUB",
        "amount": amount,
    }
    headers = {
        "apikey": API_KEY
    }

    try:
        response = requests.get(API_URL, params=params, headers=headers)
        response.raise_for_status()
        return response.json().get("result", 0.0)
    except (requests.RequestException, ValueError, KeyError):
        return 0.0
