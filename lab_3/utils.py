import os
import json

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.hazmat.primitives.serialization import load_pem_private_key


def load_config(path: str) -> dict:
    """
    Данная функция загружает данные конфигурации из JSON файла.

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


def read_binary_file(path: str) -> bytes:
    """
    Данная функция читает файл как бинарный.

    :param: path: путь к файлу
    :return: бинарный файл
    """

    try:
        with open(path, "rb") as file:
            return file.read()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Файл '{path}' не найден: {e}")
    except PermissionError as e:
        raise PermissionError(f"Нет доступа к файлу '{path}': {e}")
    except OSError as e:
        raise OSError(f"Ошибка при чтении файла '{path}': {e}")
    

def write_binary_file(path: str, data: bytes) -> None:
    """
    Данная функция записывает данные в бинарный файл.

    :param: path: путь для сохранения
    :param: data: данные для записи
    """

    try:
        with open(path, "wb") as file:
            file.write(data)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Директория '{path}' не найдена: {e}")
    except PermissionError as e:
        raise PermissionError(f"Нет доступа к файлу '{path}': {e}")
    except OSError as e:
        raise OSError(f"Ошибка при записи файла '{path}': {e}")
    

def load_private_key(path: str) -> RSAPrivateKey:
    """
    Данная функция загружает закрытый RSA ключ.

    :param: path: путь к PEM файлу с закрытым ключом
    :return: загруженный закрытый RSA ключ
    """

    try:
        private_bytes = read_binary_file(path)
        return load_pem_private_key(private_bytes, password=None)
    except ValueError as e:
        raise ValueError(f"Закрытый ключ '{path}' повреждён: {e}")
    

def save_public_key(path: str, public_key: RSAPublicKey) -> None:
    """
    Данная функция сохраняет открытый RSA ключ.

    :param: path: путь для сохранения ключа
    :param: public_key: открытый RSA ключ
    """

    key_data = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    write_binary_file(path, key_data)


def save_private_key(path: str, private_key: RSAPrivateKey) -> None:
    """
    Данная функция сохраняет закрытый RSA ключ.

    :param: path: путь для сохранения ключа
    :param: private_key: закрытый RSA ключ
    """

    key_data = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    write_binary_file(path, key_data)