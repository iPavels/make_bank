import json
import logging
import os
from typing import Any, Dict, List

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

os.makedirs("logs", exist_ok=True)


file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)


file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(file_formatter)


if not logger.handlers:
    logger.addHandler(file_handler)
    logger.propagate = False


def load_transactions(filepath: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.
    :param filepath: путь до JSON-файла
    :return: список словарей с транзакциями или пустой список
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.debug(f"Файл успешно загружен: {filepath}, количество записей: {len(data)}")
                return data
            else:
                logger.error(f"Ожидался список в файле {filepath}, но получено: {type(data)}")
    except FileNotFoundError:
        logger.error(f"Файл не найден: {filepath}")
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {filepath}")
    except Exception as e:
        logger.exception(f"Непредвиденная ошибка при загрузке файла {filepath}: {e}")

    logger.debug(f"Возвращен пустой список транзакций из {filepath}")
    return []
