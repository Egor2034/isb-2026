from asymmetric import decrypt_sym_key
from symmetric import encrypt_sym
from utils import read_binary_file, write_binary_file, load_private_key


def encrypt(
        path_original_text: str,
        path_private_key: str,
        path_sym_key: str,
        path_cipher_text: str
) -> None:
    """
    Шифрует данные с помощью алгоритма SEED.
    Симметриный ключ расшифровыется закрытым RSA ключом перед использованием.
    Результат сохраняется вместе с вектором инициализации.

    :param: path_original_text: путь к исходному тексту
    :param: path_private_key: путь к закрытому RSA ключу
    :param: path_sym_key: путь к зашифрованном симметричному ключу
    :param: path_cipher_text: путь для сохранения зашифрованного текста
    """

    enc_sym_key = read_binary_file(path_sym_key)
    text = read_binary_file(path_original_text)

    print("Загрузка закрытого ключа")
    private_key = load_private_key(path_private_key)
    print("Закрытый ключ загружен")

    print("Получение симметричного ключа")
    dec_sym_key = decrypt_sym_key(enc_sym_key, private_key)
    print("Симметричный ключ получен")

    print("Шифрование текста симметричным алгоритмом")
    iv, c_text = encrypt_sym(text, dec_sym_key)
    print("Шифрование текста завершено")
    
    print("Сохранение зашифрованного файла")
    write_binary_file(path_cipher_text, iv + c_text)
    print("Шифрование завершено")