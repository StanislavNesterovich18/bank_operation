from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_dick_executed, list_dick_canceled):

    assert filter_by_state(list_dick_executed, state='EXECUTED') == list_dick_executed
    assert filter_by_state(list_dick_canceled, state='CANCELED') == list_dick_canceled


def test_filter_by_state_not(list_dick_not_found):
    assert filter_by_state(list_dick_not_found, state='EXECUTED') == list_dick_not_found


def test_sort_by_date(list_dick_date):
    assert sort_by_date(list_dick_date, reverse=True) == list_dick_date


def test_sort_by_date_same(list_dick_date_same):
    assert sort_by_date(list_dick_date_same, reverse=True) == list_dick_date_same
