from datetime import datetime
from typing import Optional

from helpers import get_arguments_upload_backup
from service.google_api import GoogleApiService


def check_count_backup(google_api: GoogleApiService, max_count_backup: int, id_root_directory: str):
    folders = google_api.get_folders(id_root_directory)
    if len(folders) > max_count_backup:
        for folder in folders[:-max_count_backup]:
            google_api.remote_file(folder.get('id'))


def upload_backup(file_path_or_directory: str,
                  id_root_directory: str,
                  name_backup_folder: Optional[str],
                  max_count_backup: int):
    google_api = GoogleApiService()
    name_backup_folder = name_backup_folder or datetime.now().strftime("backup_server__%d_%m_%Y__%H_%M_%S")

    google_api.upload_folder(file_path_or_directory, name_backup_folder, id_root_directory)

    check_count_backup(
        google_api=google_api,
        max_count_backup=max_count_backup,
        id_root_directory=id_root_directory
    )


if __name__ == '__main__':
    arguments = get_arguments_upload_backup()
    upload_backup(
        file_path_or_directory=arguments['file_path_or_directory'],
        id_root_directory=arguments['id_root_directory'],
        name_backup_folder=arguments['name_backup_folder'],
        max_count_backup=arguments['max_count_backup']
    )
