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


if __name__ == "__main__":
    main()
