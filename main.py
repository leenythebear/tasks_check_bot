import os
from dotenv import load_dotenv

import requests


url = 'https://dvmn.org/api/user_reviews/'
load_dotenv()
token = os.environ['TOKEN']


headers = {'Authorization': f'Token {token}'}
response = requests.get(url, headers=headers)
response.raise_for_status()
print(response.text)
