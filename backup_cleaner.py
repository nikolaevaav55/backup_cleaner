import sys
import os
import pathlib
import logging

logging.basicConfig(filename='cleaner.log', filemode='w')

DIRECTORY_NAME = 'dbrldump'
PATH = pathlib.Path(__file__).parent / f"{DIRECTORY_NAME}"
MAX_FILE_LIMIT = 3


def get_file_names() -> tuple[str, str]:
    try:
        file_list = tuple(os.listdir(PATH))
        return file_list
    except FileNotFoundError as ex:
        logging.error("FileNotFoundError")


def time_date_match(file_list: tuple) -> dict:
    time_date_match = {}
    for file_name in file_list:
        file_path = os.path.join(PATH, file_name)
        creation_date = os.path.getctime(file_path)
        time_date_match[creation_date] = file_name
    return time_date_match


def get_oldest_file_name(time_date_match: dict) -> str:
    min_date = min(time_date_match.keys())
    oldest_file_name = time_date_match[min_date]
    return oldest_file_name


def delete_oldest_file(oldest_file_name):
    os.remove(f"{PATH}/{oldest_file_name}")

def delete_old_files():
    file_list = get_file_names()
    if file_list:
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
