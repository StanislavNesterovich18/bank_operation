def filter_by_state(list_slavori: list[dict], state: str = 'EXECUTED') -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению."""
    new_list = []
    for k in list_slavori:
        if k['state'] == state:
            new_list.append(k)
    return new_list


def sort_by_date(list_slavori: list[dict], reverse: bool = True) -> list[dict]:
    """Функция возвращает новый список, отсортированный по дате."""
    sorted_data = sorted(list_slavori, key=lambda x: x['date'], reverse=reverse)
    return sorted_data
