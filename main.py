import sys
import pandas as pd
import time

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from ui_main import Ui_MainWindow
# from confirm_folder import Ui_Dialog


path_csv_ves = r'\\192.168.1.98\04 inside_doc\04 Выборки данных\dir_vessels_db.csv'
path_csv_lib = r'\\192.168.1.98\02 Library'


class SearchFolder(QMainWindow):
    def __init__(self):
        super(SearchFolder, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_search_folder.clicked.connect(self.find_path)

    def find_path(self):
        data = get_data()
        data = valid_data(data)
        read_csv(path_csv_ves)



        pass

    def get_data(self):
        # 1. получить данные от пользователя
        data = self.ui.le_target.text()
        return data

    # 2. проверить на валидность данные пользователя
    def valid_data(self, data):
        last_req = []
        while '  ' in data:
            data_user = data.replace('  ', ' ')
        data_user = data.strip().lower()
        last_req.append(data)  # список с последними запросами
        save_csv('temp_csv', last_req)  # сохраняем список в файл
        print(data)
        print(last_req)
        return data_user

        # 3. прочитать файл csv
    def read_csv(self, path):
        data = pd.read_csv(path)
        return data

    # 4. выбрать пути по условию
    def sort_data(self, data):
        data = pd.read_csv(path)
        data = data[data['path'].str.contains(target)]
        # save_csv('result.csv', data)
        print(data)
        return data

        # 5. сохранить / вывести на экран
    def save_data(self):
        pass

    def refresh_data(self):
        pass

    def viewing_requests(self):
        pass

    # TODO подключить селектер выбора папок поиска:
    # - 03_пароходы_чертежи
    # - 02 Library

    # Сохраняем файл csv
    # def save_csv(path, data):
    #     df = pd.DataFrame(data, columns=['path'])
    #     df = df['path'].str.lower()
    #     df.to_csv(path, index=False)

    # 3. Читаем файл csv


    # 4. Сортируем пути по условию и сохраняем во временный файл


    # TODO: добавить логику если нет такой папки
    # если существует хотя бы один путь, показать его.
    # если нет, то вывести окно с сообщением

    # Обработчик пользовательского ввода



# if __name__ == '__main__':
#     # user_data = input('Введите название судна / папки:\n')
#
#     # @timer
#     def search_path():
#         name_folder = user_input_handler(user_data)
#         data = read_csv(path_csv)
#         sort_csv(data, name_folder)
    #
    #
    # search_path()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SearchFolder()
    window.show()
    sys.exit(app.exec())


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
