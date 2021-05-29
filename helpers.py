import sys
from argparse import ArgumentParser
from typing import Dict


def get_argument_parser_upload_backup() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('-f', '--file_path', type=str, required=True,
                        help='Путь до папки или файла который нужно сохранить.')
    parser.add_argument('-i', '--id_root_directory', type=str, required=True,
                        help='ID папки на гугл диске, куда будет записан бэкап.')
    parser.add_argument('-m', '--max_count_backup', type=int, default=1,
                        help='Максимальное количество бэкапов на гугл диске.')
    parser.add_argument('-n', '--name_backup_folder', type=str, default=None,
                        help='Имя папки создаваемой на гугл диске и которой будут лежать все с копирование файлы.')
    return parser


def get_arguments_upload_backup() -> Dict[str, any]:
    parser = get_argument_parser_upload_backup()
    arguments = parser.parse_args(sys.argv[1:])
    return {
        'file_path_or_directory': arguments.file_path,
        'id_root_directory': arguments.id_root_directory,
        'max_count_backup': arguments.max_count_backup,
        'name_backup_folder': arguments.name_backup_folder,
    }


def get_argument_parser_create_file() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('-f', '--full_path_to_file', type=str, required=True,
                        help='Полный путь до файла который нужно сохранить.')
    parser.add_argument('-i', '--folder_id', type=str, required=True,
                        help='ID папки на гугл диске, куда будет записан бэкап.')
    return parser


def get_arguments_create_file() -> Dict[str, any]:
    parser = get_argument_parser_create_file()
    arguments = parser.parse_args(sys.argv[1:])
    return {
        'full_path_to_file': arguments.full_path_to_file,
        'folder_id': arguments.folder_id,
    }
