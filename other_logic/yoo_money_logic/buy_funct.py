from yookassa import Configuration, Payment
from dotenv import load_dotenv
import os
import sys
import qrcode
import requests

# Загружаем переменные окружения
load_dotenv()

# Установите учетные данные
Configuration.account_id = os.getenv('SHOP_ID')
Configuration.secret_key = os.getenv('SECRET_KEY')


# Создание конфигуратора
def create_payment(amount, currency='RUB', description='Оплата товаров'):
    try:
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
            "description": description,
            "receipt": {
                "email": "customer_email@example.com",  # Укажите email покупателя
                "phone": "79000000000",  # Укажите телефон покупателя (может потребоваться)
                "items": [
                    {
                        "description": "Товар",  # Название товара
                        "quantity": 1,             # Количество
                        "amount": {
                            "value": str(amount),  # Сумма за товар
                            "currency": currency
                        },
                        "vat_code": 1,            # Код НДС (например, 1 - 20% для обычных товаров)
                        "payment_subject": "commodity",  # Укажите значение payment_subject
                        "payment_mode": "full_payment"   # Укажите значение payment_mode (например, "full_payment")
                    }
                ]
            }
        })
        return payment
    except Exception as e:
        print(e)


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