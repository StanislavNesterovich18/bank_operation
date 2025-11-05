# from src.processing import filter_by_state, sort_by_date
# from src.masks import get_mask_card_number, get_mask_account
# from src.widget import get_data, mask_account_card
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
