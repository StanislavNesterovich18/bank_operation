import csv
import pandas as pd


def read_csv(path: str) -> list[dict]:
    """функция чтения из .csv файла"""
    reader_list = []
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            reader_list.append(row)

    return reader_list


def read_xlsx(path: str) -> list[dict]:
    """функция чтения из excel файла"""
    df = pd.read_excel(path)
    result = df.to_dict(orient='records')
    return result
