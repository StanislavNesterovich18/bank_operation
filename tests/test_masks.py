import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "entry_value, expected",
    [
        ("2112 2112 2134 5456",
         "2112 21** **** 5456"),
        ("5474 6444 4334 1293",
         "5474 64** **** 1293")
    ]
)
def test_get_mask_card_number(entry_value, expected):
    assert get_mask_card_number(entry_value) == expected
