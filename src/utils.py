import json


def load_operations(path: str) -> list[dict]:
    """
    Чтение операций из файла
    :param path: путь к файлу
    :return: json с операциями
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)
