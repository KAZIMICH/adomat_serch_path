import sys
import pandas as pd
import csv

from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QListWidget, QAbstractItemView, QListWidgetItem
from ui_main import Ui_MainWindow

path_csv_ves = r'\\192.168.1.98\04 inside_doc\04 Выборки данных\dir_vessels_db.csv'
path_csv_lib = r'\\192.168.1.98\02 Library'


class SearchFolder(QMainWindow):
    def __init__(self):
        super(SearchFolder, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_search_folder.clicked.connect(self.search_path)

    # результат поиска путей
    def search_path(self, data):
        data = self.get_data_user()
        print(f'1 - данные пользователя в теле- {data} class - {type(data)}')
        data_user = self.data_clear(data)
        print(f'2 - после очистки в теле - {data_user} class - {type(data_user)}')

        data_db = self.read_csv(path_csv_ves)
        # print(f'3 - читаем базу в теле - {data}')
        data_find = self.data_find(data_db, data_user)
        print(f'4 - результат поиска в теле - {data} class - {type(data)}')
        data = self.save_data_csv('result.csv', data_find)
        print(data_find)
        # self.view_result_search(data)

    # 1. получить данные от пользователя, убрать лишние пробелы
    def get_data_user(self):
        data = str(self.ui.le_target.text())
        print(f'1 - данные пользователя в функции- {data} class - {type(data)}')
        return data

    # 2. убрать лишние пробелы
    def data_clear(self, data):
        data = str(data)
        data = ' '.join(data.split())
        data = data.strip()
        data = data.lower()
        print(f'2 - после очистки в функции - {data} class - {type(data)}')
        return data

    # 3. прочитать файл csv
    def read_csv(self, path):
        data = pd.read_csv(path)
        # print(f'3 - читаем базу в функции - {data}')
        return data

    # def loadCsv(self, file_name):
    #     with open(file_name, 'rb') as fileInput:
    #         for row in csv.reader(fileInput):
    #             items = [QtGui.QStandartItem(field) for field in row]
    #             self.model.appendRow(items)
    #
    # def writeCsv(self, file_name):
    #     with open(file_name, 'wb') as fileOutput:
    #         writter = csv.writter(fileOutput)
    #         for rowNumber in range(self.model.rowCount()):
    #             fields = [self.model.data(self.model.index(rowNumber, columnNumber), QtCore.Qt.DisplayRole)
    #                       for columnNumber in range(self.model.columnCount())]
    #             writer.writerow(fields)
    #
    # @QtCore.pyqtSlot()
    # def on_pushButtonLoad_clicked(self):
    #     self.loadCsv(self.filename)
    #
    # @QtCore.pyqtSlot()
    # def on_pushButtonWrite_clicked(self):
    #     self.writeCsv(self.filename)

    # 4. выбрать пути по условию
    def data_find(self, data, target):
        print(f'данные базы - {data}')
        print(f'данные искомые - {target}')
        data = data[data['path'].str.contains(target)]
        print(f'4 - результат поиска в функции - {data} class - {type(data)}')
        return data

    # 5. сохранить / вывести на экран
    def save_data_csv(self, path, data):
        df = pd.DataFrame(data, columns=['path'])
        df = df['path'].str.lower()
        df.to_csv(path, index=False)
        data = str(data)
        return data

    # вывод результата в lbl_result
    def view_result_search(self, data):
        self.lst_result.setText(self.on_pushButtonLoad_clicked)
        # listWidget = QListWidget()
        # self.ui.lst_result.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # for i in data:
        #     item = QListWidgetItem(i)
        #     listWidget.addItem(item)

    # 7. обновить данные путей
    def refresh_data(self):
        pass

    # 8. просмотреть последние запросы
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
