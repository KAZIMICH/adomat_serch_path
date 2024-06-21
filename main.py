import sys
import pandas as pd
import csv
from settings import db_file_02_paths

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QWidget, QFileDialog, QMessageBox, QPushButton

path_csv_ves = r'\\192.168.1.98\04 inside_doc\04 Выборки данных\dir_vessels_db.csv'
path_csv_lib = r'\\192.168.1.98\02 Library'


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # загружаем GUI
        uic.loadUi('ui_main.ui', self)

        # кнопка "искать"
        self.btn_search_folder.clicked.connect(self.get_result)
        # кнопка "обновить данные в базе"
        # кнопка "открыть последние запросы"

        self.data_user = []
        self.data_base = []

    # ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
    # окно уведомления
    def war_message(self, mess):
        war = QMessageBox.warning(self, 'Уведомление', mess)

    # основная функция
    def get_result(self):
        self.data_user = self.get_data_user()
        self.data_base = self.read_csv()
        print(self.data_find())

    # 1. получить данные от пользователя, убрать лишние пробелы
    # данные пользователя
    def get_data_user(self):
        data = str(self.le_user_request.text())
        # проверка пустого ввода
        if data == '':
            mess = 'Нечего искать. Вы ничего не ввели...'
            self.war_message(mess)
        else:
            # убрать лишние пробелы
            data = str(data)
            data = ' '.join(data.split()).strip().lower()
        return data

    # 2. прочитать файл csv
    def read_csv(self):
        try:
            with open(db_file_02_paths, 'rb') as my_file:
                data = pd.read_csv(my_file)
            return data
        except FileNotFoundError:
            mess = 'Файл с базой данных отсутствует.\nОбратитесь к разработчику.'
            self.war_message(mess)

    # 3. выбрать пути по условию
    def data_find(self):
        data = self.data_base
        target = self.data_user
        print(f'данные базы - {data}')
        print(f'данные искомые - {target}')
        data = data[data['path'].str.contains(target)]
        print(f'4 - результат поиска в функции - {data} class - {type(data)}')
        return data


    # 3. прочитать файл csv


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



    # # 5. сохранить / вывести на экран
    # def save_data_csv(self, path, data):
    #     df = pd.DataFrame(data, columns=['path'])
    #     df = df['path'].str.lower()
    #     df.to_csv(path, index=False)
    #     data = str(data)
    #     return data
    #
    # # вывод результата в lbl_result
    # def view_result_search(self, data):
    #     self.lst_result.setText(self.on_pushButtonLoad_clicked)
    #     # listWidget = QListWidget()
    #     # self.ui.lst_result.setSelectionMode(QAbstractItemView.ExtendedSelection)
    #     # for i in data:
    #     #     item = QListWidgetItem(i)
    #     #     listWidget.addItem(item)
    #
    # # 7. обновить данные путей
    # def refresh_data(self):
    #     pass
    #
    # # 8. просмотреть последние запросы
    # def viewing_requests(self):
    #     pass

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
    ex = App()
    ex.show()
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
