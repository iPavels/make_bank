def filter_by_currency(transactions, currency_code):
    """
    Генератор, возвращающий транзакции, где код валюты соответствует currency_code.

    """
    for transaction in transactions:
        currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if currency == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """Генератор, возвращающий по одному описанию из каждой транзакции"""
    for transaction in transactions:
        description = transaction.get("description")
        if description:
            yield description


def card_number_generator(start, stop):
    """Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        formatted = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted

