from unittest.mock import mock_open, patch
from src.utils import financial_transaction, amount_transaction


def test_financial_transaction():
    with patch("builtins.open", mock_open(read_data='{"1":"2"}')):
        assert financial_transaction("") == {"1": "2"}
    with patch("builtins.open", mock_open(read_data='{"1":"2"')):
        assert financial_transaction("") == []


def test_amount_transaction():
    with patch("requests.get") as r_mock:
        r_mock.return_value.json.return_value = {"result": 111.0}
        assert amount_transaction({"operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}}}) == 111.0
        assert amount_transaction({"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}) == 1000.0
        assert amount_transaction({}) == "Валюта не найдена"
