import imaplib
import email
from email.header import decode_header
import re
from datetime import datetime

# # Сохраняем файл в текущую директорию
# with open(filename, 'wb') as f:
#     f.write(part.get_payload(decode=True))
# print(f'Сохранено: {filename}')


class EmailClient:
    def __init__(self, username, password, imap_server):
        self.username = username
        self.password = password
        self.imap_server = imap_server
        self.imap = imaplib.IMAP4_SSL(self.imap_server)

    def login(self):
        self.imap.login(self.username, self.password)

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

    def check_emails_message(self, data: tuple):
        date_message = str(data[1])
        time_message = date_message[date_message.find(' ') + 1:date_message.rfind('+')]
        time_now_date = str(datetime.now())
        time_now_time = time_now_date[time_now_date.find(' ') + 1:time_now_date.rfind('.')]
        if (date_message[:date_message.find(' ')] == time_now_date[:time_now_date.find(' ')] \
            and abs(int(time_message[time_message.find(':') + 1:time_message.rfind(':')]) -
                    int(time_now_time[time_now_time.find(':') + 1:time_now_time.rfind(':')]))) <= 1:
            return data[0]
        else:
            return f'Сообщение не найдено'

    # Для выхода из соединения с почтовым ящиком
    def logout(self):
        self.imap.logout()


if __name__ == '__main__':
    # Использование класса
    username = 'haskytop41@mail.ru'
    password = '9qBuWnghRraj4naK5jPB'
    imap_server = 'imap.mail.ru'

    client = EmailClient(username, password, imap_server)
    client.login()

    latest_email = client.fetch_latest_email()
    if latest_email:
        attachments = client.extract_attachments(latest_email)





