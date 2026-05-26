from asymmetric import decrypt_sym_key
from symmetric import decrypt_sym
from utils import write_binary_file, read_binary_file, load_private_key


def decrypt(
        path_cipher_text: str,
        path_private_key: str,
        path_sym_key: str,
        path_dec_text: str
) -> None:
    """
    Данная функция расшифровывает файл с помощью симметричного алгоритма SEED.
    Симметричный ключ расшифровывается закрытым RSA ключом.

    :param: path_cipher_text: путь к зашифрованному тексту
    :param: path_private_key: путь к закрытому RSA ключу
    :param: path_sym_key: путь к защифрованному симметричному ключу
    :param: path_dec_text: путь для сохранения расшифрованного файла
    """

    enc_sym_key = read_binary_file(path_sym_key)

    print("Загрузка закрытого RSA ключа")
    private_key = load_private_key(path_private_key)
    print("Закрытый ключ загружен")

    print("Получение симметричного ключа")
    sym_key = decrypt_sym_key(enc_sym_key, private_key)
    print("Симметричный ключ получен")

    print("Чтение зашифрованного файла")
    data = read_binary_file(path_cipher_text)
    print("Зашифрованный файл считан")

    print("Расшифровка файла")
    iv, c_text = data[:16], data[16:]
    dec_text = decrypt_sym(iv, c_text, sym_key)
    print("Файл расшифрован")

    print("Сохранение файла")
    write_binary_file(path_dec_text, dec_text)
    print("Файл сохранён")