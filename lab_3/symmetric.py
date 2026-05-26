import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def generate_key() -> bytes:
    """
    Данная функция генерирует случайный симметричный ключ SEED длиной 128 бит
    
    :return: ключ SEED
    """
    return os.urandom(16)


def encrypt_sym(data: bytes, key: bytes) -> tuple[bytes, bytes]:
    """
    Данная функция шифрует данные алгоритмом SEED.

    :param: data: данные для шифрования в байтах
    :param: key: симметричный ключ длиной 16 байт

    :return: iv: вектор инициализации длиной 16 байт
    :return: c_text: зашифрованные данные
    """

    try:
        padder = padding.ANSIX923(128).padder()
        padded_data = padder.update(data) + padder.finalize()

        iv = os.urandom(16) 
        cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(padded_data) + encryptor.finalize()

        return iv, c_text
    except Exception as e:
        raise RuntimeError(f"Ошибка при шифровании файла: {e}")
    

def decrypt_sym(iv: bytes, c_text: bytes, key: bytes) -> bytes:
    """
    Данная функция расшифровывает данные алгоритмом SEED.

    :param: iv: вектор инициализации длиной 16 байт
    :param: c_text: зашифрованные данные
    :param: key: симметричный ключ длиной 16 байт

    :return: расшифрованные данные
    """

    try:
        cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(c_text) + decryptor.finalize()

        unpadder = padding.ANSIX923(128).unpadder()
        dc_text = unpadder.update(padded_data) + unpadder.finalize()

        return dc_text
    except Exception as e:
        raise RuntimeError(f"Ошибка при расшифровке файла: {e}")