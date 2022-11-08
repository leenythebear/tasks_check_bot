import os
import time

from dotenv import load_dotenv
import telegram

import requests
from requests import ReadTimeout, ConnectionError

url_for_long_polling = 'https://dvmn.org/api/long_polling/'
load_dotenv()


def send_requests(token):
    headers = {'Authorization': f'Token {token}'}
    timestamp = time.time()
    while True:
        try:
            response = requests.get(url_for_long_polling, headers=headers, params={'timestamp': timestamp}, timeout=90)
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


def

if __name__ == '__main__':
    load_dotenv()

    dvmn_token = os.environ['DVMN_TOKEN']
    bot_token = os.environ['BOT_TOKEN']
    chat_id = os.environ['CHAT_ID']








