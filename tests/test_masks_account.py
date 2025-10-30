import pytest

from src.masks import get_mask_account


@pytest.mark.parametrize(
    "entry_value, expected",
    [
        ("21122112213454561234",
         "**1234"),
        ("54746444433412933223",
         "**3223"),
        ("5474644443341293322",
         "Вы ввели неправильный номер счета"),
        ("",
         "Вы ввели неправильный номер счета")

    ]
)
def test_get_mask_account(entry_value, expected):
    assert get_mask_account(entry_value) == expected