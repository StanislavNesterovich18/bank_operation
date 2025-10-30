from src.processing import filter_by_state, sort_by_date


def test_filter_by_state():
    list_dictionaries = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    assert filter_by_state(list_dictionaries, state='EXECUTED') == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]
    assert filter_by_state(list_dictionaries, state='CANCELED') == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


def test_filter_by_state_not():
    list_dictionaries_no_state = [
        {'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    assert filter_by_state(list_dictionaries_no_state, state='EXECUTED') == "Данные не найдены"


def test_sort_by_date():
    list_dictionaries = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    assert sort_by_date(list_dictionaries, reverse=True) == [
        {'date': '2019-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'},
        {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
        {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
        {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}
    ]


def test_sort_by_date_same():
    list_dictionaries = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}
    ]
    assert sort_by_date(list_dictionaries, reverse=True) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}
    ]
