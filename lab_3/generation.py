from asymmetric import encrypt_sym_key, generate_rsa_keys
from symmetric import generate_sym_key
from utils import save_private_key, save_public_key, write_binary_file


def generate(
        path_sym_key: str,
        path_public_key: str,
        path_private_key: str
) -> None:
    """
    Данная функция генерирует ключ SEED и пару RSA ключей.
    Симметричный ключ шифруется открытым RSA ключом.

    :param: path_sym_key: путь к зашифрованному симметричному ключу
    :param: path_public_key: путь к открытому RSA ключу
    :param: path_private_key: путь к закрытому RSA ключу
    """

    print("Генерация симметричного ключа")
    try:
        sym_key = generate_sym_key()
    except Exception as e:
        raise RuntimeError(f"Симметричный ключ не сгенерировался: {e}")
    print("Симметричный ключ сгенерирован")

    print("Генерация открытого и закрытого RSA ключей")
    try:
        private_key, public_key = generate_rsa_keys()
    except Exception as e:
        raise RuntimeError(f"RSA ключи не сгенерировались: {e}")
    print("Открытый и закрытый RSA ключи сгенерированы")

    print("Шифрование симметричного ключа открытым RSA ключом")
    enc_sym_key = encrypt_sym_key(sym_key, public_key)
    print("Симметричный ключ сгенерирован")

    print("Сохранение зашифрованного симметричного ключа")
    write_binary_file(path_sym_key, enc_sym_key)
    print("Зашифрованный симметричный ключ сохранён")

    print("Сохранение открытого RSA ключа")
    save_public_key(path_public_key, public_key)
    print("Открытый RSA ключ сохранён")

    print("Сохранение закрытого RSA ключа")
    save_private_key(path_private_key, private_key)
    print("Закрытый RSA ключ сохранён")