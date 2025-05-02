import pytest


@pytest.fixture
def f_card_numbers() -> list[tuple[str, str]]:
    """Фикстура с тестовыми номерами карт"""
    return [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("9876543210987654", "9876 54** **** 7654"),
    ]


@pytest.fixture
def f_mask_account() -> list[tuple[str, str]]:
    """Фикстура с тестовыми номерами счета"""
    return [
        ("40817810099910004312", "**4312"),
        ("40817810444456789012", "**9012"),
        ("34679825673255761234", "**1234"),
    ]


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "description": "Перевод организации",
            "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}},
        },
        {
            "id": 2,
            "description": "Оплата",
            "operationAmount": {"amount": "500.00", "currency": {"name": "RUB", "code": "RUB"}},
        },
        {
            "id": 3,
            "description": "Перевод с карты на карту",
            "operationAmount": {"amount": "300.00", "currency": {"name": "USD", "code": "USD"}},
        },
    ]
