def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if len(card_number) != 16:
        raise ValueError("Неверная длина номера карты. Ожидалось 16 символов.")
    masks = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return masks


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if len(account_number) != 20:
        raise ValueError("Неверная длина номера счета. Ожидалось 20 символов.")
    masks = "**" + account_number[-4:]
    return masks


# print(get_mask_card_number("1234567890123456"))
