import functools
import logging
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Модуль decorators содержит декораторы для логирования функций.

    Декоратор log позволяет отслеживать вызовы функций, их параметры,
    результаты выполнения и возникающие ошибки. Логи могут выводиться
    в консоль или сохраняться в файл.
    """

    def decorator(func: Callable) -> Callable:
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        if filename:
            handler = logging.FileHandler(filename)
        else:
            handler = logging.StreamHandler()

        handler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(handler)

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            logger.info(f"Вызов функции {func.__name__} с args={args}, kwargs={kwargs}")
            try:
                result = func(*args, **kwargs)
                logger.info(f"Функция {func.__name__} завершилась с результатом: {result}")
                return result
            except Exception as e:
                logger.exception(f"Ошибка в функции {func.__name__} при вызове с args={args}, kwargs={kwargs}: {e}")
                raise

        return wrapper

    return decorator
