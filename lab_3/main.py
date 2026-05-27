import argparse

from utils import load_config
from encryption import *
from generation import *
from decryption import *

def parse_arguments() -> argparse.Namespace:
    """
    Функция, которая парсит аргументы командной строки

    :return: аргументы командной строки
    """
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-gen", "--generation", action="store_true", help="Режим генерации ключей")
    group.add_argument("-enc", "--encryption", action="store_true", help="Режим шифрования данных")
    group.add_argument("-dec", "--decryption", action="store_true", help="Режим дешифрования данных")

    parser.add_argument("--input", help="Путь к исходному файлу")
    parser.add_argument("--output", help="Путь к выходному файлу")
    parser.add_argument("--sym_key", help="Путь к симметричному ключу")
    parser.add_argument("--public_key", help="Путь к открытому RSA ключу")
    parser.add_argument("--private_key", help="Путь к закрытому RSA ключу")

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    
    settings = load_config("settings.json")
    
    path_file = args.input or settings["initial_file"]
    path_sym_key =  args.sym_key or settings["symmetric_key"]
    path_public_key = args.public_key or settings["public_key"] 
    path_private_key = args.private_key or settings["private_key"] 
    
    match args:
        case _ if args.generation:
            generate(path_sym_key, path_public_key, path_private_key)
        case _ if args.encryption:
            encrypt(
                path_file, 
                path_private_key, 
                path_sym_key, 
                args.output or settings["encrypted_file"]
            )
        case _:
            decrypt(
                args.input or settings["encrypted_file"],
                path_private_key,
                path_sym_key,
                args.output or settings["decrypted_file"]
            )


if __name__ == "__main__":
    main()