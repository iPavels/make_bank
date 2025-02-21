def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    masks = card_number[:4] + " " + card_number[6:8] + "** **** " + card_number[-4:]
    return masks


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    masks = "**" + account_number[-4:]
    return masks
