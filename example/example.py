# Источник - https://www.youtube.com/watch?v=au01t_WOe_Q
# Весь проект в теле приложения

# преобразование файла из QtDesigner в .py файл в терминале
# 1. pyside6-rcc res-rc.qrc -o res_rc.py #  файл с ресурсами
# 2. --//-- res-new-window-rc.qrc -o res_new_window-rc.py  # файл с ресурсами
# 3. pyside6-uic ui_main.ui -o ui_main.py  #  файл с графикой
# 4. --//-- new_transaction.ui -o new_transaction.py

import sys

from PySide6.QtWidgets import QApplication, QMainWindow  # использует PySide6 вместо PyQT6

from ui_main import Ui_MainWindow  # преобразованный в .py файл QtDesigner


class ExpenseTracker(QMainWindow):
    def __int__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())


