from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(dotenv_path=find_dotenv(), verbose=False, override=True)

ID_ROOT_DIRECTORY = os.getenv('ID_ROOT_DIRECTORY')
FILE_PATH = os.getenv('FILE_PATH')
MAX_COUNT_BACKUP = int(os.getenv('MAX_COUNT_BACKUP'))
