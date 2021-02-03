from datetime import datetime
from typing import Optional

from helpers import get_arguments
from service.google_api import GoogleApiService


def upload_backup(file_path_or_directory: str,
                  id_root_directory: str,
                  name_backup_folder: Optional[str]):
    google_api = GoogleApiService()
    name_backup_folder = name_backup_folder or datetime.now().strftime("backup_server__%d_%m_%Y__%H_%M_%S")
    google_api.upload_folder(file_path_or_directory, name_backup_folder, id_root_directory)


def check_count_backup(max_count_backup: int, id_root_directory: str):
    google_api = GoogleApiService()
    folders = google_api.get_folders(id_root_directory)
    if len(folders) > max_count_backup:
        for folder in folders[:-max_count_backup]:
            google_api.remote_file(folder.get('id'))


if __name__ == '__main__':
    arguments = get_arguments()
    upload_backup(file_path_or_directory=arguments['file_path_or_directory'],
                  id_root_directory=arguments['id_root_directory'],
                  name_backup_folder=arguments['name_backup_folder'])

    check_count_backup(max_count_backup=arguments['max_count_backup'],
                       id_root_directory=arguments['id_root_directory'])
