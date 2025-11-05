import pytest
from src.widget import mask_account_card


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
        ("1230 as03 3203 132s",
         "Вы ввели неправильный номер карты"),
        ("Счет 54746444983432933223",
         "Счет **3223"),
        ("Счет 547sd4444334dd9332а3",
         "Вы ввели неправильный номер счета"),
        ("",
         "Вы ввели неправильный номер карты")
    ]
)
def test_get_mask_card_number(entry_value, expected):
    assert mask_account_card(entry_value) == expected
