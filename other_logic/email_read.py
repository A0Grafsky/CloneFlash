import imaplib
import email
from email.header import decode_header
import base64
from bs4 import BeautifulSoup
import re

# Пишем свои данные
mail_pass = "9qBuWnghRraj4naK5jPB"
username = 'haskytop41@mail.ru'
imap_server = 'imap.mail.ru'
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, mail_pass)

# # Заходим в папку с сообщениями
imap.select("INBOX")

# Поиск всех непрочитанных писем
status, messages = imap.uid('search', None, 'ALL')

# Проверка на успешность поиска
if status == "OK":
    # Получаем список UID писем в обратном порядке (последнее будет первым)
    mail_ids = messages[0].split()
    if mail_ids:
        latest_mail_id = mail_ids[-1]  # Берем последний UID

        # Извлечение содержимого письма
        res, msg = imap.uid('fetch', latest_mail_id, '(RFC822)')
        msg = email.message_from_bytes(msg[0][1])



# Перебираем все части сообщения
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

            # Сохраняем файл в текущую директорию
            with open(filename, 'wb') as f:
                f.write(part.get_payload(decode=True))
            print(f'Сохранено: {filename}')

