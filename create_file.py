from helpers import get_arguments_create_file
from service.google_api import GoogleApiService


def create_file(full_path_to_file: str,
                folder_id: str):
    google_api = GoogleApiService()

    file = full_path_to_file.split('/')
    file_name = file[-1]
    file_path = '/'.join(file[0:-1])

    google_api.create_file(name=file_name, file_path=file_path, folder_id=folder_id)


if __name__ == '__main__':
    arguments = get_arguments_create_file()
    create_file(
        full_path_to_file=arguments['full_path_to_file'],
        folder_id=arguments['folder_id']
    )
