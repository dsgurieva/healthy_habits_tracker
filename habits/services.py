import requests
from django.conf import settings
from users.models import User


URL = 'https://api.telegram.org/bot'
TOKEN = settings.TELEGRAM_TOKEN


def get_updates():
    """Получает chat_id"""
    token = settings.TELEGRAM_TOKEN
    response = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
    return response.json()


def parse_updates(updates):
    """Парсит данные для получения chat_id"""
    for u in updates:
        user = User.objects.get(telegram=u['message']['chat']['username'])
        if User.objects.filter(telegram=user.telegram).exists():
            user.chat_id = u['message']['chat']['id']
            user.update_id = u['update_id']
            user.save()


def send_message(text, chat_id):
    requests.post(
        url=f'{URL}{TOKEN}/sendMessage',
        data={
            'chat_id': chat_id,
            'text': text
        }
    )
