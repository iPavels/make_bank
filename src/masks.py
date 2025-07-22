import logging
import os

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

os.makedirs("logs", exist_ok=True)


file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)


file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(file_formatter)


if not logger.handlers:
    logger.addHandler(file_handler)
    logger.propagate = False


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if len(card_number) != 16:
        logger.error("Неверная длина номера карты. Ожидалось 16 символов.")
        raise ValueError("Неверная длина номера карты. Ожидалось 16 символов.")

    masks = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    logger.debug(f"Успешно замаскирован номер карты: {masks}")
    return masks


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if len(account_number) != 20:
        logger.error("Неверная длина номера счета. Ожидалось 20 символов.")
        raise ValueError("Неверная длина номера счета. Ожидалось 20 символов.")

    masks = "**" + account_number[-4:]
    logger.debug(f"Успешно замаскирован номер счета: {masks}")
    return masks


# print(get_mask_card_number("1234567890123456"))
