def get_mask_card_number(number_card: str) -> str:
    """Функцию маскировки номера банковской карты"""
    card_namber_str = number_card.replace(" ", "")
    if len(card_namber_str) == 16:
        return card_namber_str[:4] + " " + card_namber_str[4:6] + "** **** " + card_namber_str[-4:]
    else:
        return "Вы ввели неправильный номер карты"


def get_mask_account(number_chek: str) -> str:
    """Функцию маскировки номера банковского счета"""
    chek_number_str = number_chek.replace(" ", "")
    if len(chek_number_str) == 20 and chek_number_str.isdigit():
        return "**" + chek_number_str[-4:]
    else:
        return "Вы ввели неправильный номер счета"
