# Основные библиотеки
import sys
import os
import datetime
import time
import fitz
import shutil
from dotenv import load_dotenv
from docx import Document

# PyQt6
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog,
                             QListWidget, QPushButton, QLabel, QGraphicsView, QFileDialog)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer

# Designer
from interface.menu import Ui_MainWindow
from interface.flesh_menu import Ui_Dialog
from interface.email_menu import UiDialogEmailTest
from interface.view_file import ViewPrintObject2
from interface.selecting_copies import SelectCopy
from interface.check_buy import CheckBuyForPrint
from interface.finish_menu import FinishDI
from interface.help_menu import HelpUi

# Сделанные модули
from other_logic.email_read import EmailClient
from other_logic.readusb import main, info_drive_usb, full_path_from_file
from other_logic.convert_for_docx import convert_doc_in_pdf
from other_logic.printer_module import print_file
from other_logic.yoo_money_logic import buy_funct


# Создаем класс для работы с диалоговыми окнами
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.showFullScreen()

        self.driver_usb = info_drive_usb()

        # Работа со списком виджетов
        self.listWidget = self.findChild(QListWidget, 'listWidget')
        self.refreshButton = self.findChild(QPushButton, 'refresh_button')
        self.refreshButton.clicked.connect(self.show_list_file)

        self.listWidget.itemClicked.connect(self.open_view_file)

        # Работа с кнопками
        self.close_button = self.findChild(QPushButton, 'exit_to_flesh')
        self.close_button.clicked.connect(self.exit_to_flesh)

    # Окон просмотра перед печатью
    def open_view_file(self, item):
        if item.text() != 'USB накопитель не найден':
            file = item.text()[:item.text().rfind('|') - 1]
            file_path = full_path_from_file(self.driver_usb, file)
            dialog = ViewPrint(file_path)
            dialog.exec()

    # Выход из диалогового окна
    def exit_to_flesh(self):
        self.close()

    # Поиск файлов с флешки
    def show_list_file(self):
        files = main()
        self.listWidget.clear()
        if files != 'USB накопитель не найден':
            for file in files:
                if file[file.rfind('.'):file.rfind('|') - 1] in ('.pdf', '.Docs', '.doc', '.docx'):
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
        self.listWidget.itemClicked.connect(self.open_view_file)
        self.refreshButton = self.findChild(QPushButton, 'refresh_button_email')
        self.refreshButton.clicked.connect(self.show_list_file_message)
        load_dotenv()
        self.folder1 = os.getenv('DIR_NAME')
        # self.folder1 = r'C:\ArsenyBelykh\ProjectLavr\CloneFlash\buffer_dir'

        # Почта для отправки файлов
        self.libel = self.findChild(QLabel, 'label_2')
        load_dotenv()
        username = os.getenv('LOGIN_NAME')
        self.libel.setText(username)
        self.libel.setStyleSheet("font: 9pt \"Microsoft YaHei UI\";\n"
                                 "color:White; \n"
                                 "font-size: 40px;\n"
                                 "background-color:rgb(83, 83, 83);\n"
                                 "border: 2px solid black")
        # Работа с кнопками
        self.exit_button = self.findChild(QPushButton, 'exit_button')
        self.exit_button.clicked.connect(self.exit_in_main)

    # Показ файлов из сообщения
    def show_list_file_message(self):
        client = self.client
        self.listWidget.clear()
        latest_email = client.fetch_latest_email()
        if latest_email:
            attachments = client.check_emails_message(client.extract_attachments(latest_email))
            for file in attachments:
                if file[file.rfind('.'):] in ('.pdf', '.Docs', '.doc', '.docx') and file != 'Сообщение не найдено':
                    self.listWidget.addItem(file)
                else:
                    self.listWidget.addItem('Сообщение не найдено')
                    break

    # Открытие окна просмотра
    def open_view_file(self, item):
        if item.text() != 'Сообщение не найдено':
            file = item.text().strip()
            file_path = self.client.save_file_from_email(file, self.folder1)
            dialog = ViewPrint(file_path)
            dialog.exec()

    def exit_in_main(self):
        self.close()
        window = ExpenseTracker()
        window.show()

    # Регистрация почты
    def login_in_email(self):
        load_dotenv()
        username = os.getenv('LOGIN_NAME')
        password = os.getenv('PASSWORD')
        imap_server = os.getenv('IMAP_SERVER')
        client = EmailClient(username, password, imap_server)
        client.login()
        return client


# Окно для работы с предпросмотром
class ViewPrint(QDialog):
    def __init__(self, filepath):
        super().__init__()
        self.ui_mail = ViewPrintObject2()
        self.ui_mail.setupUi(self)
        self.showFullScreen()

        self.file_path = filepath

        self.exit_button = self.findChild(QPushButton, 'exit_button_from_print')
        self.exit_button.clicked.connect(self.exit_in_list_file)
        self.left_button = self.findChild(QPushButton, 'left_button')
        self.left_button.clicked.connect(self.show_previous_page)
        self.right_button = self.findChild(QPushButton, 'right_button')
        self.right_button.clicked.connect(self.show_next_page)

        self.print_button = self.findChild(QPushButton, 'print_button')
        self.print_button.clicked.connect(self.open_print_window)

        self.image_label = self.findChild(QLabel, 'file_view')
        self.image_label.setScaledContents(True)

        # Держим информацию о текущем изображении
        self.current_page_index = -1
        self.image_pages = []

        # Папка для фоток
        load_dotenv()
        self.folder = os.getenv('DIR_NAME')
        self.load_file(filepath)

    def load_file(self, filepath):
        """Загружает содержимое файла в текстовую область."""
        if os.path.exists(filepath):
            ext = os.path.splitext(filepath)[1].lower()
            if ext == '.pdf':
                self.load_pdf(filepath)
            else:
                self.load_pdf(convert_doc_in_pdf(filepath, self.folder))

        else:
            QMessageBox.warning(self, "Ошибка", "Файл не найден!")

    def load_pdf(self, filepath):
        """Загружает содержимое файла .pdf как изображение."""
        doc = fitz.open(filepath)
        self.image_pages.clear()

        # Конвертируем каждую страницу PDF в изображение
        for page in doc:
            pix = page.get_pixmap()  # Получаем растровое изображение страницы
            img_file = f"{self.folder}/page_{page.number}.png"
            pix.save(img_file)  # Сохраняем изображение на диск
            self.image_pages.append(img_file)  # Добавляем путь к изображению в список
        # Показ первой страницы
        if self.image_pages:
            self.current_page_index = 0
            self.display_page(self.current_page_index)

    def display_page(self, page_index):
        """Отображает указанную страницу."""
        if 0 <= page_index < len(self.image_pages):
            pixmap = QPixmap(self.image_pages[page_index])
            self.image_label.setPixmap(pixmap)

    def show_previous_page(self):
        """Показать предыдущую страницу."""
        if self.current_page_index > 0:
            self.current_page_index -= 1
            self.display_page(self.current_page_index)

    def show_next_page(self):
        """Показать следующую страницу."""
        if self.current_page_index < len(self.image_pages) - 1:
            self.current_page_index += 1
            self.display_page(self.current_page_index)

    def exit_in_list_file(self):
        # Указание директории
        buffer_dir = self.folder  # Убедитесь, что self.folder содержит правильный путь
        try:
            # Проверяем, существует ли папка
            if os.path.exists(buffer_dir):
                # Удаляем все файлы и папки внутри buffer_dir
                shutil.rmtree(buffer_dir)
                # Создаем папку заново
                os.makedirs(buffer_dir)
                self.close()
        except Exception as e:
            print(f"Произошла ошибка при очистке папки: {e}")
            self.close()

    # Открытие окна оплаты
    def open_print_window(self):
        print_window = PriceAndCopy(len(self.image_pages), self.file_path)
        print_window.exec()


# Окно выбора копий и оплаты
class PriceAndCopy(QDialog):
    def __init__(self, image_pages, file_path):
        try:
            super().__init__()
            self.ui_mail = SelectCopy()
            self.ui_mail.setupUi(self)
            self.showFullScreen()

            self.file_path = file_path

            self.buy_button = self.findChild(QPushButton, 'buy_button')
            self.buy_button.clicked.connect(self.open_check_buy_window)

            self.exit_button = self.findChild(QPushButton, 'exit_button_from_print')
            self.exit_button.clicked.connect(self.exit_in_view)

            self.up_button = self.findChild(QPushButton, 'right_button')
            self.up_button.clicked.connect(self.up_number_for_copy)

            self.down_button = self.findChild(QPushButton, 'left_button')
            self.down_button.clicked.connect(self.down_number_for_copy)

            self.number_copy = self.findChild(QLabel, 'price_display_2')
            self.text_number = self.number_copy.text()[
                               self.number_copy.text().find('">') + 2:self.number_copy.text().rfind("</p")]
            self.number_copy.setText(self.text_number)

            load_dotenv()
            self.price_copy = os.getenv('PRICE_COPY')
            self.price_display = self.findChild(QLabel, 'price_display')
            self.price_copy = str(int(self.price_copy) * image_pages)
            self.price_display.setText(self.price_copy)

        except Exception as e:
            print(e)

    # Выход из меню оплаты
    def exit_in_view(self):
        self.close()

    # Добавить копии
    def up_number_for_copy(self):
        if int(self.text_number) <= 4:
            self.text_number = str(int(self.text_number) + 1)
            self.number_copy.setText(self.text_number)
            self.change_price()

    # Убрать копии
    def down_number_for_copy(self):
        if int(self.text_number) >= 2:
            self.text_number = str(int(self.text_number) - 1)
            self.number_copy.setText(self.text_number)
            self.change_price()

    # Работа с ценами
    def change_price(self):
        new_price = int(self.price_copy) * int(self.text_number)
        self.price_display.setText(str(new_price))

    def open_check_buy_window(self):
        # функция по оплате тут
        amount = self.price_display.text()
        check_buy_window = CheckBuy(amount, self.file_path)
        check_buy_window.exec()


class CheckBuy(QDialog):
    def __init__(self, amount, file_path):
        super().__init__()
        self.ui_mail = CheckBuyForPrint()
        self.ui_mail.setupUi(self)
        self.showFullScreen()
        try:
            # Виджеты
            self.qrcode_display = self.findChild(QLabel, 'qrcode_photo')
            self.qrcode_display.setScaledContents(True)

            self.file_path = file_path

            self.status_bar = self.findChild(QLabel, 'status_bar')

            # Вытаскиваем url и id оплаты
            payment_url, payment_id = buy_funct.get_payment_url(amount)

            # Генерация и загрузка QR-кода
            buy_funct.generate_qr_code(payment_url)
            pixmap = QPixmap("payment_qr.png")
            self.qrcode_display.setPixmap(pixmap)

            self.check_buy_button = self.findChild(QPushButton, 'check_buy_button')
            self.check_buy_button.clicked.connect(lambda: self.check_payment(payment_id))
            self.exit_button = self.findChild(QPushButton, 'exit_button_from_list_file')
            self.exit_button.clicked.connect(self.exit_from_window)
        except Exception as e:
            print(e)

    def exit_from_window(self):
        self.close()

    # Проверка оплаты
    def check_payment(self, payment_id):
        payment_status = buy_funct.check_payment_status(payment_id)
        if payment_status is not None:
            if payment_status in 'pending':
                self.status_bar.setText('ОЖИДАНИЕ')
            elif payment_status in 'succeeded':
                self.status_bar.setText('УСПЕШНО')
                QTimer.singleShot(2000, lambda: self.show_dialog())
        else:
            self.status_bar.setText('Ошибка')

    # Показ финального окна + закрытие предыдущих окон
    def show_dialog(self):
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, QDialog) and widget.isVisible():
                widget.close()
        dialog = FinishMenu(self.file_path)
        dialog.exec()


class FinishMenu(QDialog):
    def __init__(self, file_path):
        super().__init__()
        self.ui_mail = FinishDI()
        self.ui_mail.setupUi(self)
        self.showFullScreen()

        try:
            # Отправляем на печать
            self.file_path = file_path
            print_file(self.file_path)

            load_dotenv()
            self.folder = os.getenv('DIR_NAME')

            buffer_dir = self.folder

            # Проверяем, существует ли папка
            if os.path.exists(buffer_dir):
                # Удаляем все файлы и папки внутри buffer_dir
                shutil.rmtree(buffer_dir)
                # Создаем папку заново
                os.makedirs(buffer_dir)
        except Exception as e:
            load_dotenv()
            self.folder = os.getenv('DIR_NAME')

            # Убедитесь, что buffer_dir определен
            buffer_dir = self.folder  # Пример: выбираем buffer_dir из переменной folder

            # Проверяем, существует ли папка
            if os.path.exists(buffer_dir):
                # Удаляем все файлы и папки внутри buffer_dir
                shutil.rmtree(buffer_dir)
                # Создаем папку заново
                os.makedirs(buffer_dir)
            print(f"Произошла ошибка при очистке папки: {e}")

        # Таймер для автоматического закрытия окна через 5 секунд
        QTimer.singleShot(5000, self.close)


# Окно помощи
class HelpMenu(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_mail = HelpUi()
        self.ui_mail.setupUi(self)
        self.showFullScreen()

        self.exit_button = self.findChild(QPushButton, 'pushButton')
        self.exit_button.clicked.connect(self.exit_window)

    def exit_window(self):
        self.close()


# Создаем класс для работы с основным окном
class ExpenseTracker(QMainWindow, QWidget):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showFullScreen()

        self.ui.help_button.clicked.connect(self.show_help_window)

        self.ui.flesh_button.clicked.connect(self.show_dialog)
        self.ui.email_button.clicked.connect(self.show_dialog_email)

    def show_dialog(self):
        dialog = Dialog()
        dialog.exec()

    def show_help_window(self):
        dialog_help = HelpMenu()
        dialog_help.exec()

    def show_dialog_email(self):
        dialog_email = DialogEmail()
        dialog_email.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    sys.exit(app.exec())
