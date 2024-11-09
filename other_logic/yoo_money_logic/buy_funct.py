from yookassa import Configuration, Payment
from dotenv import load_dotenv
import os
import sys
import qrcode
import requests

# Загружаем переменные окружения
load_dotenv()

# Установите учетные данные
Configuration.account_id = os.getenv('Shop_ID')
Configuration.secret_key = os.getenv('SECRET_KEY')

# Создание конфигуратора
def create_payment(amount, currency='RUB', description='Оплата товаров'):
    payment = Payment.create({
        "amount": {
            "value": str(amount),
            "currency": currency
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://your_return_url.com"  # Укажите URL, куда вернется пользователь после оплаты
        },
        "capture": True,
        "description": description
    })
    return payment


# Создание нового платежа
def get_payment_url(amount, currency='RUB', description='Оплата товаров'):
    payment = create_payment(amount, currency, description)
    return payment.confirmation.confirmation_url, payment.id


# Проверка платежа
def check_payment_status(payment_id):
    try:
        payment = Payment.find_one(payment_id)
        return payment.status
    except Exception as e:
        print(f"Ошибка при проверке статуса платежа: {e}")
        return None


# Создание qr_coda
def generate_qr_code(url):
    qr = qrcode.make(url)
    qr.save("payment_qr.png")