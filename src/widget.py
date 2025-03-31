from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """Функция принимает строку с типом и номером карты или счета, возвращает замаскированный номер."""
    parts = input_string.split()
    card_or_account_type = " ".join(parts[:-1])
    number = parts[-1]

    if card_or_account_type.startswith("Счет"):
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{card_or_account_type} {masked_number}"


def get_date(date: str) -> str:
    """Функция возвращает дату"""
    date_object = datetime.fromisoformat(date)
    formatted_date = date_object.strftime("%d.%m.%Y")
    return formatted_date


# print(mask_account_card("Visa 1234567812345678"))
