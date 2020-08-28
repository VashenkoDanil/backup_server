from datetime import datetime

from service.google_api import GoogleApiService
from settings.project import FILE_PATH, MAX_COUNT_BACKUP


def upload_backup():
    google_api = GoogleApiService()
    name_backup_folder = datetime.now().strftime("backup_server__%d_%m_%Y__%H_%M_%S")
    google_api.upload_folder(FILE_PATH, name_backup_folder)


def check_count_backup():
    google_api = GoogleApiService()
    folders = google_api.get_backup_folder()
    if len(folders) > MAX_COUNT_BACKUP:
        for folder in folders[:-MAX_COUNT_BACKUP]:
            google_api.remote_file(folder.get('id'))


if __name__ == '__main__':
    check_count_backup()
    upload_backup()
