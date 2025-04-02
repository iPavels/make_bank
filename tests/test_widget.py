from src.widget import get_date, mask_account_card
import pytest


@pytest.mark.parametrize("input_string, expected", [
    ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
    ("Счет 12345678901234567890", "Счет **7890"),
    ("MasterCard 9876543210987654", "MasterCard 9876 54** **** 7654"),
])
def test_mask_account_card(input_string, expected):
    assert mask_account_card(input_string) == expected


def test_get_date() -> None:
    assert get_date("2025-03-31T10:15:30") == "31.03.2025"
    assert get_date("2000-01-01T00:00:00") == "01.01.2000"
    assert get_date("1999-12-31T23:59:59") == "31.12.1999"
