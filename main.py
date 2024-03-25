import pandas as pd
import time
from ui_QTD6 import Ui_MainWindow


path_csv = r'\\192.168.1.98\04 inside_doc\04 Выборки данных\dir_vessels_db.csv'

# class MainWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
# 
#         self.dir = None
#         self.textEdit = QtWidgets.QTextEdit()
#         self.listWidget = QtWidgets.QListWidget()
# 
#         vbox = QVBoxLayout(self)
#         vbox.addWidget(self.textEdit)
#         vbox.addWidget(self.listWidget)
# 
#         self.select_ws()

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


# Сохраняем файл csv
# def save_csv(path, data):
#     df = pd.DataFrame(data, columns=['path'])
#     df = df['path'].str.lower()
#     df.to_csv(path, index=False)


# 3. Читаем файл csv
def read_csv(path):
    data = pd.read_csv(path)
    return data


# 4. Сортируем пути по условию и сохраняем во временный файл
def sort_csv(data, target):
    data = data[data['path'].str.contains(target)]
    # save_csv('result.csv', data)
    return data

# TODO: добавить логику если нет такой папки
# если существует хотя бы один путь, показать его.
# если нет, то вывести окно с сообщением


# Обработчик пользовательского ввода
def user_input_handler(data):
    last_req = []
    while '  ' in data:
        data = data.replace('  ', ' ')
    data = data.strip().lower()
    last_req.append(data)  # список с последними запросами
    save_csv('temp_csv', last_req)  # сохраняем список в файл
    return data


if __name__ == '__main__':
    user_data = input('Введите название судна / папки:\n')
    @timer
    def search_path():
        name_folder = user_input_handler(user_data)
        data = read_csv(path_csv)
        sort_csv(data, name_folder)

    search_path()


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     w = MainWindow()
#     w.show()
#     sys.exit(app.exec())


# TODO Прикрутить PyQt6

# дата и время создания файла:
# import os
# from datetime import datetime
#
# filename = "test.txt"
# stat = os.stat(filename)
# ctime = stat.st_ctime
# ctime_readable = datetime.fromtimestamp(ctime)
# print(ctime_readable)