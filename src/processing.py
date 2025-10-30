from typing import Union


def filter_by_state(list_dictionaries: Union[list[dict]], state: Union[str] = 'EXECUTED') -> Union[list[dict], str]:
    """Функция возвращает новый список словарей."""
    new_list = []
    for k in list_dictionaries:
        if 'state' in k:
            if k['state'] == state:
                new_list.append(k)
    if not new_list:
        return "Данные не найдены"
    return new_list


def sort_by_date(list_dictionaries: list[dict], reverse: bool = True) -> list[dict]:
    """Функция возвращает новый список, отсортированный по дате."""
    sorted_data = sorted(list_dictionaries, key=lambda x: x['date'], reverse=reverse)
    return sorted_data
