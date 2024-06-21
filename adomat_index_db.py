import os
import pandas as pd
import time

folder = r'\\192.168.1.98\03_пароходы_чертежи'
path_db = r'\\192.168.1.98\04 inside_doc\04 DB\02 paths'
name_csv = 'dir_vessels_db.csv'


# Функция - декоратор
def timer(func):
    def wrapper(*args, **kwargs):
        # start the timer
        start_time = time.time()
        # call the decorated function
        result = func(*args, **kwargs)
        # remeasure the time
        end_time = time.time()
        # compute the elapsed time and print it
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        # return the result of the decorated function execution
        return result
    # return reference to the wrapper function
    return wrapper


# 1. Получаем перечень путей к папкам
def get_dirs_paths(directory):
    return [os.path.join(root) for root, _, files in os.walk(directory)]

# TODO Прикрутить проверку и игнорирование папок на доступность


# 2. Сохраняем список путей в файл в нижнем регистре
def save_csv(path, name, data):
    df = pd.DataFrame(data, columns=['path'])
    df = df['path'].str.lower()
    df.to_csv(os.path.join(path, name))


if __name__ == '__main__':
    @timer
    def index_db():
        paths = get_dirs_paths(folder)
        save_csv(path_db, name_csv, paths)

    index_db()


# TODO 
# 1. В виртуальном окружении устанавливаем PyInstaller
# 2. Открываем через терминал директорию с проектом
# 3. Запускаем pyinstaller --onefile --noconsole имя файла с расширением
# 	где --onefile упаковка в 1 файл; --noconsole не запускать консоль
# 4. В папке с проектом создана новая папка dist, там находится файл exe