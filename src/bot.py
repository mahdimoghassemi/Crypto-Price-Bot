import requests
from config.settings import BOT_TOKEN, CHANNEL_ID

def send_message(text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHANNEL_ID,
        'text': text
    }
    response = requests.post(url, data=payload)
    return response.json()