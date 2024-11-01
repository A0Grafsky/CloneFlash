# import os
# import win32api
# import win32print
#
#
# def print_file(file_path):
#     if os.path.isfile(file_path):
#         # Получаем имя принтера
#         printer_name = win32print.GetDefaultPrinter()
#
#         # Отправляем файл на печать
#         win32api.ShellExecute(0, "print", file_path, None, ".", 0)
#         print(f'Файл {file_path} отправлен на печать через принтер {printer_name}.')
#     else:
#         print(f'Файл {file_path} не найден!')
#
#
# # Пример использования
# print_file('C:\ArsenyBelykh\ProjectLavr\CloneFlash\ТЗ RealPet.pdf')

import os
import win32api
import win32print


def print_file(file_path, copies=1):
    if os.path.isfile(file_path):
        # Получаем имя принтера
        printer_name = win32print.GetDefaultPrinter()

        # Открываем принтер
        hprinter = win32print.OpenPrinter(printer_name)
        try:
            # Создаем структуру для задания параметров печати
            job_info = (
                os.path.basename(file_path),  # Имя документа
                None,                          # Выводной файл
                'RAW'                          # Тип данных
            )

            # Отправляем файл на печать с указанным количеством копий
            win32print.StartDocPrinter(hprinter, 1, job_info)
            win32print.StartPagePrinter(hprinter)

            for _ in range(copies):
                win32api.ShellExecute(0, "print", file_path, None, ".", 0)

            win32print.EndPagePrinter(hprinter)
            win32print.EndDocPrinter(hprinter)

            print(f'Файл {file_path} отправлен на печать через принтер {printer_name}. Копий: {copies}.')
        finally:
            win32print.ClosePrinter(hprinter)
    else:
        print(f'Файл {file_path} не найден!')


# Пример использования


if __name__ == '__main__':
    print_file('C:\\ArsenyBelykh\\ProjectLavr\\CloneFlash\\ТЗ RealPet.pdf', copies=2)





