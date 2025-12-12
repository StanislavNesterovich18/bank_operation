import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/masks.log', "w", "utf-8")
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_card: str) -> str:
    """Функцию маскировки номера банковской карты"""
    logger.info("запуск функции get_mask_card_number")
    card_namber_str = number_card.replace(" ", "")
    if len(card_namber_str) == 16:
        logger.info("замаскированный номер карты")
        return card_namber_str[:4] + " " + card_namber_str[4:6] + "** **** " + card_namber_str[-4:]
    else:
        logger.error("ошибка: неправильный номер карты")
        return "Вы ввели неправильный номер карты"


def get_mask_account(number_chek: str) -> str:
    """Функцию маскировки номера банковского счета"""
    logger.info("запуск функции get_mask_account")
    number_chek.isdigit()
    chek_number_str = number_chek.rsplit(" ", 1)[-1]
    if len(chek_number_str) == 20:
        logger.info("замаскированный номер счета")
        return "**" + chek_number_str[-4:]
    else:
        logger.error("ошибка: неправильный номер счета")
        return "Вы ввели неправильный номер счета"
