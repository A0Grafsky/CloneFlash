from dotenv import load_dotenv
import subprocess
import os
import time
load_dotenv()

key = os.getenv('LOGIN_NAME')

# Укажите путь к QuickLook.exe
quicklook_path = r'C:\Program Files\WindowsApps\21090PaddyXu.QuickLook_3.7.3.0_neutral__egxr34yet59cg\Package\QuickLook.exe'

def open_quicklook(file_path):
    if os.path.exists(quicklook_path):
        try:
            process = subprocess.Popen([quicklook_path, file_path])  # Открываем QuickLook в фоновом режиме
            return process
        except Exception as e:
            print("Произошла ошибка при запуске QuickLook:", e)
    else:
        print("QuickLook.exe не найден!")

# Запрос пути к файлу у пользователя
file_path = r'ТЗ RealPet.pdf'  # Укажите полный путь к файлу

if os.path.exists(file_path):
    process = open_quicklook(file_path)
    if process:
        print("QuickLook открыт. Вы можете продолжать использовать приложение.")
        # Здесь могут быть другие действия или даже ожидание, если вы хотите, чтобы приложение продолжало работать
        try:
            # Пример: ждать, пока пользователь не завершит работу с приложением
            while process.poll() is None:
                time.sleep(1)  # Мы просто ждем, не забирая ресурсы
        except KeyboardInterrupt:
            print("Завершение работы приложения.")
else:
    print("Файл не найден. Пожалуйста, проверьте правильность введенного пути.")

# def open_view_file(file_path):
