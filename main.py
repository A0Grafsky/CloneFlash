import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog,
                             QListWidget, QPushButton)

from interface.menu import Ui_MainWindow
from interface.flesh_menu import Ui_Dialog
from interface.email_menu import Ui_Dialog_email
from other_logic.readusb import main


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
        self.close_button = self.findChild(QPushButton, 'exit_to_flesh')
        self.close_button.clicked.connect(self.exit_to_flesh)

    def exit_to_flesh(self):
        self.close()

    def show_list_file(self):
        files = main()
        self.listWidget.clear()
        if files != 'USB накопитель не найден':
            for file in files:
                self.listWidget.addItem(file)
        else:
            self.listWidget.addItem("USB накопитель не найден")


class DialogEmail(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_mail = Ui_Dialog_email()
        self.ui_mail.setupUi(self)

        self.exit_button = self.findChild(QPushButton, 'exit_button')
        self.exit_button.clicked.connect(self.exit_in_main)

    def exit_in_main(self):
        self.close()
        window = ExpenseTracker()
        window.show()


# Создаем класс для работы с основным окном
class ExpenseTracker(QMainWindow, QWidget):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.flesh_button.clicked.connect(self.show_dialog)
        self.ui.email_button.clicked.connect(self.show_dialog_email)

    def show_dialog(self):
        dialog = Dialog()
        dialog.exec()

    def show_dialog_email(self):
        dialog_email = DialogEmail()
        dialog_email.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    sys.exit(app.exec())
