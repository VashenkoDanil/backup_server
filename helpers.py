import sys
from argparse import ArgumentParser
from typing import Dict


def create_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('-f', '--file_path', type=str, required=True,
                        help='Путь то папки или файла который нужно сохранить.')
    parser.add_argument('-i', '--id_root_directory', type=str, required=True,
                        help='ID папки на гугл диске, куда будет записан бэкап.')
    parser.add_argument('-m', '--max_count_backup', type=int, default=1,
                        help='Максимальное количество бэкапов на гугл диске.')
    parser.add_argument('-n', '--name_backup_folder', type=str, default=None,
                        help='Имя папки создаваемой на гугл диске и которой будут лежать все с копирование файлы.')
    return parser


def get_arguments() -> Dict[str, any]:
    parser = create_parser()
    arguments = parser.parse_args(sys.argv[1:])
    return {
        'file_path_or_directory': arguments.file_path,
        'id_root_directory': arguments.id_root_directory,
        'max_count_backup': arguments.max_count_backup,
        'name_backup_folder': arguments.name_backup_folder,
    }
