import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(f_card_numbers: list[tuple[str, str]]) -> None:
    for input_string, expected in f_card_numbers:
        assert get_mask_card_number(input_string) == expected

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("987654321012345")

    assert str(exc_info.value) == "Неверная длина номера карты. Ожидалось 16 символов."


def test_get_mask_account(f_mask_account: list[tuple[str, str]]) -> None:
    for input_string, expected in f_mask_account:
        assert get_mask_account(input_string) == expected

    with pytest.raises(ValueError) as exc_info:
        get_mask_account("7365410843013587430")

    assert str(exc_info.value) == "Неверная длина номера счета. Ожидалось 20 символов."
