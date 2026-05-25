import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def generate_key() -> bytes:
    """Данная функция генерирует случайный симметричный ключ SEED длиной 128 бит"""
    random_key = os.urandom(16)


def encrypt_sym(data: bytes, key: bytes) -> 