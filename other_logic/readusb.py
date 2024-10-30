import os
import wmi


# Находим драйвер подключенной флешки
def info_drive_usb():
    c = wmi.WMI()
    logical_disks = c.query('SELECT * FROM Win32_LogicalDisk')
    if logical_disks:
        for disk in logical_disks:
            if disk.DriveType == 2:
                return disk.Caption


# def full_path_from_file(usb_drive, item):
#     if not os.path.exists(usb_drive):
#         print(f"USB drive {usb_drive} не найден.")
#         return
#     # Проходим по всем директориям и файлам на USB
#     for root, dirs, files in os.walk(usb_drive):
#         for file in files:
#             file_path = os.path.join(root, file)
#             if item in file_path:
#                 return file_path


def list_files_from_usb(usb_drive):
    mas_files = []
    if not os.path.exists(usb_drive):
        print(f"USB drive {usb_drive} не найден.")
        return
    # Проходим по всем директориям и файлам на USB
    for root, dirs, files in os.walk(usb_drive):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            full_file = f'{file} | {file_size}КБ'
            mas_files.append(full_file)
    return mas_files


def main():
    usb_drives = info_drive_usb()
    if usb_drives:
        # Читаем файлы с первого найденного USB-диска
        # print(f"Список фалов с {usb_drives}")
        return list_files_from_usb(info_drive_usb())
    else:
        return f'USB накопитель не найден'


def full_path_from_file(usb_drive, item):
    if not usb_drive.endswith('\\'):
        usb_drive += '\\'

    # Приводим usb_drive к стандартному формату с '/' в качестве разделителей
    usb_drive = os.path.normpath(usb_drive)

    if not os.path.exists(usb_drive):
        print(f"USB drive {usb_drive} не найден.")
        return None

    # Проходим по всем директориям и файлам на USB
    for root, dirs, files in os.walk(usb_drive):
        for file in files:
            file_path = os.path.join(root, file)
            # Проверяем полное совпадение, а не просто наличие подстроки
            if os.path.basename(file_path) == item:
                return file_path
    print(f"Файл '{item}' не найден на USB.")
    return None


if __name__ == "__main__":
    # print(info_drive_usb())
    print(full_path_from_file(info_drive_usb(), ''))
