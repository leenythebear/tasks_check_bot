import os
import time

from dotenv import load_dotenv
import telegram

import requests
from requests import ReadTimeout, ConnectionError

url_for_long_polling = 'https://dvmn.org/api/long_polling/'
load_dotenv()


def check_lessons_review(token, chat_id, bot):
    headers = {'Authorization': f'Token {token}'}
    params = {}
    while True:
        try:
            response = requests.get(url_for_long_polling, headers=headers, params=params, timeout=60)
            response.raise_for_status()
            timestamp = response.json()['last_attempt_timestamp']
            # response = requests.get(url_for_long_polling, headers=headers, , timeout=5)
            # response.raise_for_status()
            print(response.text)
        except ReadTimeout:
            continue
        except ConnectionError:
            continue
        time.sleep(90)


def send_message(chat_id, bot, review):
    new_attempts = review['new_attempts'][0]
    if not new_attempts['is_negative']:
        message = 'Вашу работу проверили, преподаватель принял работу'
        bot.send_message(chat_id=chat_id, text=message)
    else:
        message = 'Вашу работу проверили, преподаватель нашел ошибки'
        bot.send_message(chat_id=chat_id, text=message)


if __name__ == '__main__':
    load_dotenv()

    dvmn_token = os.environ['DVMN_TOKEN']
    bot_token = os.environ['BOT_TOKEN']
    chat_id = os.environ['CHAT_ID']








