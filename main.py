import sys
import os

from dotenv import load_dotenv
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog,
                             QListWidget, QPushButton)

from interface.menu import Ui_MainWindow
from interface.flesh_menu import Ui_Dialog
from interface.email_menu import UiDialogEmailTest
from other_logic.email_read import EmailClient
from other_logic.readusb import main


# Создаем класс для работы с диалоговыми окнами
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.showFullScreen()

        # Работа со списком виджетов
        self.listWidget = self.findChild(QListWidget, 'listWidget')
        self.refreshButton = self.findChild(QPushButton, 'refresh_button')
        self.refreshButton.clicked.connect(self.show_list_file)

        # Работа с кнопками
        self.close_button = self.findChild(QPushButton, 'exit_to_flesh')
        self.close_button.clicked.connect(self.exit_to_flesh)

    # Выход из диалогового окна
    def exit_to_flesh(self):
        self.close()

    # Поиск файлов с флешки
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
        self.ui_mail = UiDialogEmailTest()
        self.ui_mail.setupUi(self)
        self.showFullScreen()
        # Аккаунт почты
        self.client = self.login_in_email()

        # Работа со списком виджетов
        self.listWidget = self.findChild(QListWidget, 'listWidget_email')
        self.refreshButton = self.findChild(QPushButton, 'refresh_button_email')
        self.refreshButton.clicked.connect(self.show_list_file_message)

        # Работа с кнопками
        self.exit_button = self.findChild(QPushButton, 'exit_button')
        self.exit_button.clicked.connect(self.exit_in_main)

    def show_list_file_message(self):
        client = self.client
        latest_email = client.fetch_latest_email()
        if latest_email:
            attachments = client.extract_attachments(latest_email)
            for file in attachments:
                self.listWidget.addItem(file)

    def exit_in_main(self):
        self.close()
        window = ExpenseTracker()
        window.show()

    def login_in_email(self):
        load_dotenv()
        username = os.getenv('LOGIN_NAME')
        password = os.getenv('PASSWORD')
        imap_server = os.getenv('IMAP_SERVER')
        client = EmailClient(username, password, imap_server)
        client.login()
        return client


# Создаем класс для работы с основным окном
class ExpenseTracker(QMainWindow, QWidget):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showFullScreen()

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
