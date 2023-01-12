import sys
import os
import pathlib
import logging

logging.basicConfig(filename='../cleaner.log', filemode='w')

DIRECTORY_NAME = 'dbrldump'
PATH = pathlib.Path(__file__).parent / f"{DIRECTORY_NAME}"
print(PATH)
MAX_FILE_LIMIT = 3


def get_file_names(path=PATH) -> tuple[str, str]:
    try:
        file_list = tuple(os.listdir(path))
        return file_list
    except FileNotFoundError as ex:
        logging.error("FileNotFoundError")
        return ()


def time_date_match(file_list: tuple, path=PATH) -> dict:
    if file_list:
        time_date_match = {}
        for file_name in file_list:
            file_path = os.path.join(path, file_name)
            creation_date = os.path.getctime(file_path)
            time_date_match[creation_date] = file_name
        return time_date_match
    else:
        return


def get_oldest_file_name(time_date_match: dict) -> str:
    if time_date_match:
        min_date = min(time_date_match.keys())
        oldest_file_name = time_date_match[min_date]
        return oldest_file_name
    else:
        return ""


def delete_oldest_file(oldest_file_name, path=PATH):
    if oldest_file_name:
        try:
            os.remove(f"{path}/{oldest_file_name}")
        except Exception as ex:
            logging.error(f"{ex}")
            return ""
    else:
        return ""

def delete_old_files():
    file_list = get_file_names()
    if file_list:
        logging.warning(f"file_list:{file_list}")
        while len(file_list) > MAX_FILE_LIMIT:
            time_date_dict = time_date_match(file_list)
            oldest_file_name = get_oldest_file_name(time_date_dict)
            delete_oldest_file(oldest_file_name)
            logging.warning(f"{oldest_file_name} deleted")
            file_list = get_file_names()
    else:
        logging.warning("Directory is empty")
    return 0


if __name__ == '__main__':
    sys.exit(delete_old_files())
