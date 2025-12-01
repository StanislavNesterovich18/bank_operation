import requests
import os
from dotenv import load_dotenv
from typing import Any

load_dotenv()


def api_currency(currency_from: list[dict], currency_amount: list[dict]) -> Any:
    """Функция конвертирует валюту в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_from}&amount={currency_amount}"

    headers = {
        "apikey": os.getenv("API_KEY_APILAYER")
    }

    response = requests.get(url, headers=headers, data={})

    result = float(response.json().get("result"))
    return result
