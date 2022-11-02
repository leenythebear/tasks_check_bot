import os
from dotenv import load_dotenv

import requests
from requests import ReadTimeout, ConnectionError

url = 'https://dvmn.org/api/user_reviews/'
url_for_long_polling = 'https://dvmn.org/api/long_polling/'
load_dotenv()
token = os.environ['TOKEN']

while True:
    headers = {'Authorization': f'Token {token}'}
    try:
        response = requests.get(url_for_long_polling, headers=headers, timeout=5)
        response.raise_for_status()
        print(response.text)
    except ReadTimeout:
        continue
    except ConnectionError:
        continue


