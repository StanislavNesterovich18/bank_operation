from src.widget import get_data


def test_get_data():
    assert get_data("2024-03-11T02:26:18.671407") == "11.03.2024"
