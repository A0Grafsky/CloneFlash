
import subprocess
import os
import time

# Укажите путь к QuickLook.exe
quicklook_path = (r'C:\Program Files\WindowsApps\21090PaddyXu.'
                  r'QuickLook_3.7.3.0_neutral__egxr34yet59cg\Package\QuickLook.exe')

# def open_quicklook(file_path):
#     if os.path.exists(quicklook_path):
#         try:
#             process = subprocess.Popen([quicklook_path, file_path])  # Открываем QuickLook в фоновом режиме
#             return process
#         except Exception as e:
#             print("Произошла ошибка при запуске QuickLook:", e)
#     else:
#         print("QuickLook.exe не найден!")


# Запрос пути к файлу у пользователя
file_path = r'../ТЗ RealPet.pdf'  # Укажите полный путь к файлу

#
# if os.path.exists(file_path):
#     process = open_quicklook(file_path)
#     if process:
#         print("QuickLook открыт. Вы можете продолжать использовать приложение.")
#         # Здесь могут быть другие действия или даже ожидание, если вы хотите, чтобы приложение продолжало работать
#         try:
#             # Пример: ждать, пока пользователь не завершит работу с приложением
#             while process.poll() is None:
#                 time.sleep(1)  # Мы просто ждем, не забирая ресурсы
#         except KeyboardInterrupt:
#             print("Завершение работы приложения.")
# else:
#     print("Файл не найден. Пожалуйста, проверьте правильность введенного пути.")


# Функция для открытия смотра файла перед печатью
def open_view_file(file_path):
    if os.path.exists(quicklook_path):
        try:
            process = subprocess.Popen([quicklook_path, file_path])  # Открываем QuickLook в фоновом режиме
            if process:
                try:
                    # Пример: ждать, пока пользователь не завершит работу с приложением
                    while process.poll() is None:
                        time.sleep(1)  # Мы просто ждем, не забирая ресурсы
                except KeyboardInterrupt:
                    return f"Завершение работы приложения."
            else:
                print("Файл не найден. Пожалуйста, "
                      "проверьте наличие или работоспособность файла.")

        except Exception as e:
            return f("Произошла ошибка при запуске QuickLook:", e)
    else:
        return f("QuickLook.exe не найден!")


