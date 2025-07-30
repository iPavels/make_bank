import logging
import os
from logging import Logger


def get_logger(name: str, filename: str) -> Logger:
    os.makedirs("logs", exist_ok=True)
    log_path = os.path.join("logs", filename)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")  # перезаписывает
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False  # Не передает выше

    return logger
