import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog,
                             QListWidget, QPushButton)

from interface.menu import Ui_MainWindow
from interface.flesh_menu import Ui_Dialog
from readusb import main


# Создаем класс для работы с диалоговыми окнами
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Работа со списком файлов
        self.listWidget = self.findChild(QListWidget, 'listWidget')
        self.refreshButton = self.findChild(QPushButton, 'refresh_button')
        self.refreshButton.clicked.connect(self.show_list_file)

    def show_list_file(self):
        files = main()
        self.listWidget.clear()
        if files != 'USB накопитель не найден':
            for file in files:
                self.listWidget.addItem(file)
        else:
            self.listWidget.addItem("USB накопитель не найден")


# Создаем класс для работы с основным окном
class ExpenseTracker(QMainWindow, QWidget):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.flesh_button.clicked.connect(self.show_dialog)

    def show_dialog(self):
        dialog = Dialog()
        dialog.exec()








if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    sys.exit(app.exec())
