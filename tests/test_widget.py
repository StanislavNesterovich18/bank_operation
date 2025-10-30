import pytest

from src.widget import mask_account_card, get_data


def test_mask_account_card():
    assert mask_account_card("счет 21122112213454561234") == "Счет **1234"
    assert mask_account_card("visa 2112211221345456") == "visa 2112 21** **** 5456"
    assert mask_account_card("") == "Вы ввели неправильный номер карты"


@pytest.mark.parametrize(
    "entry_value, expected",
    [
        ("Mastercard 2112211221345456",
         "Mastercard 2112 21** **** 5456"),
        ("Visa Classik 5474644443341293",
         "Visa Classik 5474 64** **** 1293"),
        ("1230 2303 3203 132",
         "Вы ввели неправильный номер карты"),
        ("",
         "Вы ввели неправильный номер карты")
    ]
)
def test_get_mask_card_number(entry_value, expected):
    assert mask_account_card(entry_value) == expected
