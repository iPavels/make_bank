def filter_by_currency(transactions, currency_code):
    """
    Генератор, возвращающий транзакции, где код валюты соответствует currency_code.

    """
    for transaction in transactions:
        currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if currency == currency_code:
            yield transaction


def transaction_descriptions():
    pass


def card_number_generator():
    pass