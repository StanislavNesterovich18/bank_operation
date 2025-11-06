def filter_by_currency(transactions, currency):
    for transact in transactions:
        if transact["operationAmount"]["currency"]["code"] == currency:
            yield transact


def transaction_descriptions(transactions):
    for transact in transactions:
        yield transact["description"]


def card_number_generator(start, end):
    for x in range(start, end + 1):
        card_number = f"{x:016d}"
        card_number_str = " ".join([card_number[x: x + 4] for x in range(0, 16, 4)])
        yield card_number_str


