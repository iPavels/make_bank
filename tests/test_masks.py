import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("987654321012345")

    assert str(exc_info.value) == "Неверная длина номера карты. Ожидалось 16 символов."


def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'

    with pytest.raises(ValueError) as exc_info:
        get_mask_account("7365410843013587430")

    assert str(exc_info.value) == "Неверная длина номера счета. Ожидалось 20 символов."
