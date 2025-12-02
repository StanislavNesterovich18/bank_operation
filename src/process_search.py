def process_bank_search(data: list[dict], search: str = "EXECUTED") -> list[dict]:
    """ Функция фильтрует словари по состоянию операции: выполнена/отменена """
    operation_bank = []
    for d in data:
        if d["state"] == search:
            operation_bank.append(d)
    return operation_bank


def process_bank_operations(data: list[dict], search: bool = True) -> list[dict]:
    """ функция сортирует по дате операции """
    search_state = sorted(data, key=lambda x: x["date"], reverse=search)

    return search_state
