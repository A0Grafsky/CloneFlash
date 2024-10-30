import imaplib
import email
import os
from dotenv import load_dotenv
from email.header import decode_header
import re
from datetime import datetime


class EmailClient:
    def __init__(self, username, password, imap_server):
        self.username = username
        self.password = password
        self.imap_server = imap_server
        self.imap = imaplib.IMAP4_SSL(self.imap_server)

    # Регистрация
    def login(self):
        self.imap.login(self.username, self.password)

    # Достаём сообщения из почты
    def fetch_latest_email(self, folder="INBOX"):
        # Заходим в указанную папку с сообщениями
        self.imap.select(folder)

        # Поиск всех писем
        status, messages = self.imap.uid('search', None, 'ALL')
        if status == "OK":
            # Получаем список UID писем в обратном порядке (последнее будет первым)
            mail_ids = messages[0].split()
            if mail_ids:
                latest_mail_id = mail_ids[-1]  # Берем последний UID

                # Извлечение содержимого письма
                res, msg = self.imap.uid('fetch', latest_mail_id, '(RFC822)')
                if res == "OK":
                    return email.message_from_bytes(msg[0][1])
        return None

    # Достаём вложения из сообщения
    def extract_attachments(self, msg):
        list_files_from_email = []

        # Получаем время отправления
        date_header = msg.get('date')
        if date_header:
            # Парсим дату
            try:
                date_sent = email.utils.parsedate_to_datetime(date_header)
            except Exception as e:
                print(f"Ошибка при парсинге даты: {e}")
                date_sent = None
        else:
            date_sent = None

        # Проходимся по сообщению
        for part in msg.walk():
            if part.get_content_disposition() == 'attachment':
                filename = part.get_filename()
                # Далее декодируем имя
                if filename:
                    filename = decode_header(filename)[0][0]
                    if isinstance(filename, bytes):
                        filename = filename.decode()
                    # Убираем лишние символы
                    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
                    list_files_from_email.append(filename)

        return list_files_from_email, date_sent

    # Проверка актуальности сообщения
    def check_emails_message(self, data: tuple):
        date_message = str(data[1])
        time_message = date_message[date_message.find(' ') + 1:date_message.rfind('+')]
        time_now_date = str(datetime.now())
        time_now_time = time_now_date[time_now_date.find(' ') + 1:time_now_date.rfind('.')]
        if (date_message[:date_message.find(' ')] == time_now_date[:time_now_date.find(' ')]) and abs(
                int(time_message[time_message.find(':') + 1:time_message.rfind(':')]) - int(
                        time_now_time[time_now_time.find(':') + 1:time_now_time.rfind(':')])) <= 1:
            return data[0]
        else:

            return f'Сообщение не найдено'

    # Сохранение выбранного файла
    def save_file_from_email(self, file, dir_file):
        msg = self.fetch_latest_email()
        for part in msg.walk():
            # Проверяем, есть ли вложение
            if part.get_content_disposition() == 'attachment':
                # Получаем имя вложения
                filename = part.get_filename()

                # Декодируем имя файла, если оно закодировано
                if filename:
                    filename = decode_header(filename)[0][0]
                    if isinstance(filename, bytes):
                        filename = filename.decode()

                # Очищаем имя файла от недопустимых символов
                if filename:
                    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)

                    # Проверяем, что имя файла не пустое
                    if filename and filename.strip():
                        # Проверка совпадения имен файла
                        if filename == file:

                            # Формирование полного пути к файлу
                            try:
                                file_path = os.path.join(dir_file, filename)
                                with open(file_path, 'wb') as f:
                                    f.write(part.get_payload(decode=True))
                                return file_path
                            # Сохраняем файл в указанную директорию
                            except Exception as e:
                                print(e)
                        else:
                            return f'Имена файлов не совпадают'
                    else:
                        return f'Ошибка, имя файла не доступно'

    # Для выхода из соединения с почтовым ящиком
    def logout(self):
        self.imap.logout()


if __name__ == '__main__':
    load_dotenv()
    username = os.getenv('LOGIN_NAME')
    password = os.getenv('PASSWORD')
    imap_server = os.getenv('IMAP_SERVER')

    # Использование класса
    client = EmailClient(username, password, imap_server)
    client.login()

    latest_email = client.fetch_latest_email()
    if latest_email:
        attachments = client.extract_attachments(latest_email)
