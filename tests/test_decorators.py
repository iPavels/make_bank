import logging

import pytest

from src.decorators import log


@log()
def add(a, b):
    return a + b


@log()
def fail_func():
    raise ValueError("Test error")


def test_log_success(caplog):
    with caplog.at_level(logging.INFO):
        result = add(2, 3)
    assert result == 5
    assert "Вызов функции add" in caplog.text
    assert "завершилась с результатом: 5" in caplog.text


def test_log_exception(caplog):
    with caplog.at_level(logging.INFO):
        with pytest.raises(ValueError):
            fail_func()
    assert "Ошибка в функции fail_func" in caplog.text
    assert "Test error" in caplog.text
