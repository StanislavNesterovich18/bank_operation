import json
import os
import re
import logging
from collections import Counter
from src.external_api import api_currency
from typing import Any

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/utils.log', "w", "utf-8")
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def financial_transaction(file_path: str = "") -> list[dict]:
    """Функция открывает json файл"""
    logger.info("Запуск функции financial_transaction")
    if file_path == "":
        utils_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(utils_dir, "..", "data", "operations.json")
        logger.info("Путь до файла json")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info("Открытие файла json в python")
        return data
    except FileNotFoundError as e:
        logger.error(f"ошибка {e}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"ошибка {e}")
        return []
    except Exception as e:
        logger.error(f"ошибка {e}")
        return []


def amount_transaction(transactions: dict) -> Any:
    """функция выводит сумму транзакции"""
    logger.info("Запуск функции amount_transaction")
    if transactions.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB':  # type: ignore
        logger.info("Возвращает сумму транзакции")
        currency_rub = float(transactions['operationAmount']['amount'])
        return currency_rub  # type: ignore
    elif transactions.get('operationAmount', {}).get('currency', {}).get('code', None) is None:  # type: ignore
        logger.error("Валюта не найдена")
        return "Валюта не найдена"  # type: ignore
    else:
        convert_currency = api_currency(transactions['operationAmount']['currency']['code'],  # type: ignore
                                        transactions['operationAmount']['amount'])  # type: ignore
        logger.info("Возвращает сумму транзакции конвертируя в рубли")

        return convert_currency


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """функция фильтрует список операций по заданным словам"""
    list_search = []
    pattern = re.compile(search, re.IGNORECASE)
    for d in data:
        if pattern.search(str(d.get("description", ""))):
            list_search.append(d)
    return list_search


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
а возвращает словарь,в котором ключи — это названия категорий,
а значения — это количество операций в каждой категории
"""
    count_categories = []
    for operation in data:
        if operation.get("description", "") in categories:
            count_categories.append(operation.get("description", ""))
    return dict(Counter(count_categories))
