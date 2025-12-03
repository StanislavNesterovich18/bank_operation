from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions_currency):
    gen_usd = filter_by_currency(transactions_currency, "USD")
    gen_rub = filter_by_currency(transactions_currency, "RUB")
    assert next(gen_usd) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "amount": "9824.07",
        "currency_name": "USD",
        "currency_code": "USD",
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(gen_usd) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "amount": "79114.93",
        "currency_name": "USD",
        "currency_code": "USD",
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(gen_rub) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "amount": "43318.34",
        "currency_name": "руб.",
        "currency_code": "RUB",
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(gen_rub) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "amount": "67314.70",
        "currency_name": "руб.",
        "currency_code": "RUB",
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


def test_transaction_descriptions(transactions_currency):
    descript_operation = transaction_descriptions(transactions_currency)
    assert next(descript_operation) == "Перевод организации"
    assert next(descript_operation) == "Перевод со счета на счет"


def test_card_number_generator():
    card_number = card_number_generator(3453344536345345, 3453453634353456)
    assert next(card_number) == "3453 3445 3634 5345"
    assert next(card_number) == "3453 3445 3634 5346"
    assert next(card_number) == "3453 3445 3634 5347"
    assert next(card_number) == "3453 3445 3634 5348"
    assert next(card_number) == "3453 3445 3634 5349"
