import sys
import os
from PyQt6 import QtWidgets, uic

# Загрузка UI, созданного в Qt Designer
class FileListApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(FileListApp, self).__init__()
        uic.loadUi('your_ui_file.ui', self)  # Убедитесь, что файл .ui правильно указан

        # Найдите элементы интерфейса по имени
        self.listWidget = self.findChild(QtWidgets.QListWidget, 'listWidget')  # Замените на имя вашего виджета
        self.refreshButton = self.findChild(QtWidgets.QPushButton, 'refreshButton')  # Замените на имя кнопки
        self.refreshButton.clicked.connect(self.refresh_file_list)

    def get_files_from_usb(self, drive_path):
        try:
            return os.listdir(drive_path)
        except Exception as e:
            print(f"Ошибка: {e}")
            return []

    def refresh_file_list(self):
        drive_path = "E:\\"  # Укажите путь к флешке
        files = self.get_files_from_usb(drive_path)
        self.listWidget.clear()
        for file in files:
            self.listWidget.addItem(file)

app = QtWidgets.QApplication(sys.argv)
window = FileListApp()
window.show()
sys.exit(app.exec())
