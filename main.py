# from src.processing import filter_by_state, sort_by_date
# from src.masks import get_mask_card_number, get_mask_account
# from src.widget import get_data, mask_account_card
# from typing import Literal

# from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
# from src.utils import financial_transaction
# from src.utils import amount_transaction
# from src.process_search import process_bank_search, process_bank_operations
#
# if __name__ == '__main__':
#     x = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#
#     print(filter_by_state(x, state='EXECUTED'))
#
#     print(sort_by_date(x, reverse=True))
#
# if __name__ == '__main__':
#     x = ""
#     print(get_mask_card_number(x))
#
# if __name__ == '__main__':
#     x = "54746444433412933222"
#     print(get_mask_account(x))
#
# if __name__ == '__main__':
#     print(mask_account_card("visa 2202002200220022"))
#
# if __name__ == '__main__':
#     print(get_data(" "))
# #
# transactions = (
#     [
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702"
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188"
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {
#                 "amount": "43318.34",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160"
#         },
#         {
#             "id": 895315941,
#             "state": "EXECUTED",
#             "date": "2018-08-19T04:27:37.904916",
#             "operationAmount": {
#                 "amount": "56883.54",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод с карты на карту",
#             "from": "Visa Classic 6831982476737658",
#             "to": "Visa Platinum 8990922113665229"
#         },
#         {
#             "id": 594226727,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "operationAmount": {
#                 "amount": "67314.70",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Visa Platinum 1246377376343588",
#             "to": "Счет 14211924144426031657"
#         }
#     ]
# )
#
# if __name__ == '__main__':
#     x = filter_by_currency(transactions, "USD")
#     print(next(x))
#     print(next(x))
#     print(next(x))
# y = transaction_descriptions(transactions)
# print(next(y))
# print(next(y))
# z = card_number_generator(3453344536345345, 3453453634353456)
# print(next(z))
# print(next(z))
# print(next(z))
# print(next(z))
# print(next(z))
#
# if __name__ == '__main__':
#     file_path = []
# print(financial_transaction())
#
# if __name__ == '__main__':
#     y = {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702"
#         }
#     y_2 = {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {
#                 "amount": "43318.34",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160"
#         }
#
#
# print(amount_transaction(y))
# print(amount_transaction(y_2))
#
# if __name__ == '__main__':
#     data =[
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702"
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188"
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {
#                 "amount": "43318.34",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160"
#         },
#         {
#             "id": 895315941,
#             "state": "EXECUTED",
#             "date": "2018-08-19T04:27:37.904916",
#             "operationAmount": {
#                 "amount": "56883.54",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод с карты на карту",
#             "from": "Visa Classic 6831982476737658",
#             "to": "Visa Platinum 8990922113665229"
#         },
#         {
#             "id": 594226727,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "operationAmount": {
#                 "amount": "67314.70",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Visa Platinum 1246377376343588",
#             "to": "Счет 14211924144426031657"
#         }
#     ]
#     search = "EXECUTED"
#
# print(process_bank_search(data,search))
#
import os
import sys

# Добавляем путь к папке src
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from generators import filter_by_currency  # type: ignore
from processing import filter_by_state, sort_by_date  # type: ignore
from read_csv_xlsx import read_csv, read_xlsx  # type: ignore
from utils import financial_transaction, amount_transaction, process_bank_search  # type: ignore
from widget import get_data, mask_account_card  # type: ignore


def main():
    user_input = input("""Привет!
Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
- """)
    transactions_list = []
    while True:
        if user_input == "1":
            transactions_list = financial_transaction("data/operation.json")
            print("Для обработки выбран JSON-файл")
            break
        elif user_input == "2":
            transactions_list = read_csv("data/transactions.csv")
            print("Для обработки выбран CSV-файл")
            break
        elif user_input == "3":
            transactions_list = read_xlsx("data/transactions_excel.xlsx")
            print("Для обработки выбран XLSX-файл")
            break
        else:
            user_input = input("не верный ввод, повторите")
    while True:
        user_input = input("""
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
- """).upper()
        if user_input in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions_list = filter_by_state(transactions_list, state=user_input)
            print(f"Операции отфильтрованы по статусу {user_input}")
            break
        else:
            print(f"Статус операции {user_input} недоступен")

    user_input = input("Отсортировать операции по дате? Да/Нет - ").lower()

    if user_input == "да":
        while True:
            user_input = input("Отсортировать по возрастанию или по убыванию? - ").lower()
            if user_input == "по возрастанию":
                sorting = False
            elif user_input == "по убыванию":
                sorting = True
            else:
                print("не корректный ввод, попробуйте снова")
                continue
            transactions_list = sort_by_date(transactions_list, reverse=sorting)
            break

    user_input = input("Выводить только рублевые транзакции? Да/Нет - ").lower()

    if user_input == "да":
        transactions_list = list(filter_by_currency(transactions_list, "RUB"))

    user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет - ").lower()
    if user_input == "да":
        user_input = input("введите фильтр - ")
        transactions_list = process_bank_search(transactions_list, user_input)

    len_transaktion = len(transactions_list)
    if len_transaktion == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций")
        print(f"Всего банковских операций в выборке: {len_transaktion}")
        for transaction in transactions_list:
            data_transaction = get_data(transaction["date"])
            print(f"{data_transaction} {transaction['description']}")
            card_to = mask_account_card(transaction["to"])
            if transaction["from"] == "":
                print(card_to)
            else:
                card_from = mask_account_card(transaction["from"])
                print(f"{card_from} -> {card_to}")
            print(f"Сумма: {transaction['amount']} {transaction['currency_code']}")
            print()


if __name__ == "__main__":
    main()
