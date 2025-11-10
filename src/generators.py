from typing import Iterator, Generator, Literal


def filter_by_currency(transactions: list, currency: Literal["USD", "RUB"]) -> Iterator:
    """
Функция возвращать итератор, который поочередно выдает транзакции,где валюта операции соответствует заданной
    """
    for transact in transactions:
        if transact["operationAmount"]["currency"]["code"] == currency:
            yield transact


def transaction_descriptions(transactions: list) -> Iterator:
    """
Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    """
    for transact in transactions:
        yield transact["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """
Генератор может сгенерировать номера карт в заданном диапазоне
    """
    for x in range(start, end + 1):
        card_number = f"{x:016d}"
        card_number_str = " ".join([card_number[x: x + 4] for x in range(0, 16, 4)])
        yield card_number_str
