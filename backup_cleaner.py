import os
import datetime
import pathlib


DIRECTORY_NAME = 'dbrldump'
PATH = pathlib.Path(__file__).parent / f"{DIRECTORY_NAME}"
MAX_FILE_LIMIT = 3


def delete_old_backup(path=PATH):
    dirs_list = os.listdir(path)
    while len(dirs_list) > MAX_FILE_LIMIT:
        try:
            my_list = sorted([x[8:24] for x in dirs_list])
            min_date = min(my_list, key=lambda i: datetime.datetime.strptime(i, '%Y-%m-%d-%H-%M'))
            os.remove(f"{PATH}/dbrldip-{min_date}.sql")
            dirs_list = os.listdir(path)
            print("Удалена папка: ", min_date)
        except Exception as error:
            print("Произошла ошибка: ", error)

            break


if __name__ == '__main__':
    delete_old_backup()


