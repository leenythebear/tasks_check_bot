import os
import time

from dotenv import load_dotenv
import telegram

import requests
from requests import ReadTimeout, ConnectionError

long_polling_url = "https://dvmn.org/api/long_polling/"


def check_lessons_review(token, chat_id, bot):
    headers = {"Authorization": f"Token {token}"}
    params = {}
    while True:
        try:
            response = requests.get(
                long_polling_url, headers=headers, params=params,
            )
            response.raise_for_status()
            lessons_review = response.json()
            if lessons_review["status"] == "timeout":
                params["timestamp"] = lessons_review["timestamp_to_requests"]
            else:
                params["timestamp"] = lessons_review["last_attempt_timestamp"]

                send_message(chat_id, bot, lessons_review)
        except ReadTimeout:
            continue
        except ConnectionError:
            time.sleep(60)


def send_message(chat_id, bot, review):
    new_attempts = review["new_attempts"][0]
    lesson_title = new_attempts["lesson_title"]
    lesson_url = new_attempts["lesson_url"]
    if not new_attempts["is_negative"]:
        message = f'Вашу работу "{lesson_title}" проверили, преподаватель ' \
                   f'принял работу: {lesson_url}'
        bot.send_message(chat_id=chat_id, text=message)
    else:
        message = f'Вашу работу "{lesson_title}" проверили, преподаватель ' \
                  f'нашел ошибки: {lesson_url} '
        bot.send_message(chat_id=chat_id, text=message)


if __name__ == "__main__":
    load_dotenv()

    dvmn_token = os.environ["DVMN_TOKEN"]
    bot_token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHAT_ID"]

    bot = telegram.Bot(token=bot_token)
    check_lessons_review(dvmn_token, chat_id, bot)
