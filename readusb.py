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


# Чтение данных с флешки
def read_files_from_usb(usb_drive):
    if not os.path.exists(usb_drive):
        print(f"USB drive {usb_drive} не найден.")
        return
    for root, dirs, files in os.walk(usb_drive):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Файл: {file_path}")
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(content)  # Обработка данных по вашему усмотрению
            except Exception as e:
                print(f"Не удалось прочитать файл {file_path}: {e}")


def main():
    usb_drives = info_drive_usb()
    if usb_drives:
        # Читаем файлы с первого найденного USB-диска
        print(f"\nЧтение файлов с  устройства {usb_drives}")
        read_files_from_usb(usb_drives)
    else:
        print("USB-накопители не найдены.")


if __name__ == "__main__":
    main()
