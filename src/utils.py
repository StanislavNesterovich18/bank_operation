import json
import os
from src.external_api import api_currency


def financial_transaction(file_path: str = "") -> list[dict]:
    """Функция открывает json файл"""
    if file_path == "":
        utils_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(utils_dir, "..", "data", "operations.json")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception:
        return []


def amount_transaction(transactions: list[dict]) -> list[dict]:
    """Функция возвращает сумму транзакции в рублях"""
    if transactions.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB':  # type: ignore
        return transactions['operationAmount']['amount']  # type: ignore
    elif transactions.get('operationAmount', {}).get('currency', {}).get('code', None) is None:  # type: ignore
        return "Валюта не найдена"  # type: ignore
    else:
        convert_currency = api_currency(transactions['operationAmount']['currency']['code'],  # type: ignore
                                        transactions['operationAmount']['amount'])  # type: ignore
        return convert_currency
