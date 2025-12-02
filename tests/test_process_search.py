from src.process_search import process_bank_search, process_bank_operations


def test_filter_by_state(operation, state_CANCELED, state_EXECUTED):
    assert process_bank_search(operation, search="CANCELED") == state_CANCELED
    assert process_bank_search(operation, search="EXECUTED") == state_EXECUTED


def test_process_bank_operations(operation, date_true, date_false):
    assert process_bank_operations(operation, search=True) == date_true
    assert process_bank_operations(operation, search=False) == date_false
