import os
import json


def load_config(path: str) -> dict:
    """
    Загружает данные конфигурации из JSON файла.

    :param: path: путь к JSON файлу
    :return: данные из JSON файла
    """

    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except OSError as error:
        print(f"Ошибка при считывании JSON: {error}")
    except Exception as error:
        print("Unexpected {error=}, {type(error)=}")
        raise