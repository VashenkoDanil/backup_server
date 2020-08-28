import mimetypes
import os
from dataclasses import dataclass, field

from google.oauth2 import service_account
from googleapiclient.discovery import build, Resource
from googleapiclient.http import MediaFileUpload

from settings.google_api import SCOPES, SERVICE_ACCOUNT_FILE
from settings.project import ID_ROOT_DIRECTORY


@dataclass
class GoogleApiService:
    service: Resource = field(init=False)

    def __post_init__(self):
        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        self.service = build('drive', 'v3', credentials=credentials)

    def get_backup_folder(self) -> list:
        query = f"'{ID_ROOT_DIRECTORY}' in parents " \
                f"and mimeType='application/vnd.google-apps.folder'" \
                f"and name contains 'backup_server'"
        results = self.service.files().list(pageSize=1000,
                                            fields="nextPageToken, files(id, name, mimeType, parents, createdTime)",
                                            q=query,
                                            orderBy="createdTime").execute()
        return results.get('files')

    def create_folder(self, name_folder: str, parents_folder: str) -> str or list:
        folder_metadata = {'name': name_folder,
                           'parents': [parents_folder],
                           'mimeType': 'application/vnd.google-apps.folder'}
        folder = self.service.files().create(body=folder_metadata, fields='id').execute()
        return folder.get('id', [])

    def create_file(self, name, root, folder_id) -> None:
        file_metadata = {'name': name, 'parents': [folder_id]}
        media = MediaFileUpload(
            os.path.join(root, name),
            mimetype=mimetypes.MimeTypes().guess_type(name)[0])
        self.service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()

    def upload_folder(self, folder_path, name_folder) -> None:
        parents_id = {}

        for root, _, files in os.walk(folder_path, topdown=True):
            last_dir = root.split('/')[-1]
            pre_last_dir = root.split('/')[-2]
            if pre_last_dir not in parents_id.keys():
                pre_last_dir = self.create_folder(name_folder, ID_ROOT_DIRECTORY)
            else:
                pre_last_dir = parents_id[pre_last_dir]

            id_folder = self.create_folder(last_dir, pre_last_dir)

            for name in files:
                self.create_file(name, root, id_folder)

            parents_id[last_dir] = id_folder

    def remote_file(self, file_id) -> None:
        self.service.files().delete(fileId=file_id).execute()
