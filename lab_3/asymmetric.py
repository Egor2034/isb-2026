from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding, rsa
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey

from utils import load_private_key, read_binary_file


def generate_rsa_keys() -> tuple[RSAPrivateKey, RSAPublicKey]:
    """
    Данная функци генерирует пару RSA ключей.

    :return: закрытый и открытый RSA ключи
    """

    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    return private_key, public_key


def encrypt_sym_key(sym_key: bytes, public_key: RSAPublicKey) -> bytes:
    """"
    Данная функция шифрует симметричный ключ открытым RSA ключом.

    :param: sym_key: симметричный ключ
    :param: public_key: открытый RSA ключ 
    
    :return: зашифрованный симметричный ключ
    """

    return public_key.encrypt(
        sym_key,
        asym_padding.OAEP(
            mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )


def decrypt_sym_key(enc_sym_key: bytes, private_key: RSAPrivateKey) -> bytes:
    """"
    Данная функция расшифровывает симметричный ключ закрытым RSA ключом.

    :param: enc_sym_key: зашифрованный симметричный ключ
    :param: private_key: закрытый RSA ключ 
    
    :return: расшифрованный симметричный ключ
    """

    return private_key.decrypt(
        enc_sym_key,
        asym_padding.OAEP(
            mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )