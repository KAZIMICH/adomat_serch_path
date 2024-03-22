import sys
import os
import pandas as pd
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QVBoxLayout


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.dir = None
        self.textEdit = QtWidgets.QTextEdit()
        self.listWidget = QtWidgets.QListWidget()

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.textEdit)
        vbox.addWidget(self.listWidget)

        self.select_ws()
        # self.process()

    # декоратор измерения времени работы
    def timemeter(self):
        import datetime

        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            result = self(*args, **kwargs)
            end_time = datetime.datetime.now()
            elapsed_time = end_time - start_time
            print(f"Затраченное время: {elapsed_time}")
            return result

        return wrapper

    @timemeter
    def select_ws(self):
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбери директорию",
                                                              r'\\192.168.1.98\03_пароходы_чертежи')

        # name_ship = input('Введите название судна')
        name_ship = 'ICE GLACIER'

        self.textEdit.setPlainText(self.dir)
        if self.dir:
            for root, dirs, files in os.walk(self.dir):
                if name_ship in dirs:
                    path = os.path.join(root, name_ship)
                    path = path.replace('/', '\\')
                    self.listWidget.addItem(path)

    # def process(self):
    #     list_item = [self.listWidget.item(row).text() for row in range(self.listWidget.count())]
    #     print(*list_item, sep='\n')
    #
    #     data = pd.DataFrame(dict(
    #         Путь=[self.dir],
    #         Список=[list_item]))
    #     print(data)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
