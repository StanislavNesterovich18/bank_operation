from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_namber: str) -> str:
    """ функция которая умеет обрабатывать информацию как о картах, так и о счетах."""
    card_namber_str = card_namber.replace(" ", "")
    if "счет" in card_namber_str.lower():
        return f"Счет {get_mask_account(card_namber_str[-20:])}"
    elif card_namber_str[-16:].isdigit():
        if len(card_namber_str) >= 16:
            return f"{card_namber[:-16]}{get_mask_card_number(card_namber_str[-16:])}"
        else:
            return "Вы ввели неправильный номер карты"
    else:
        return "Вы ввели неправильный номер карты"


def get_data(time_card: str) -> str:
    """принимает системную дату/время, возвращает дату в формате ДД.ММ.ГГГГ"""
    return time_card[8:10] + "." + time_card[5:7] + "." + time_card[:4]
