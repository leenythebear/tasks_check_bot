# Бот для отправки оповещений о результе код-ревью на сайте [dvmn.org](https://dvmn.org/)

## Как установить

1. Скачайте код
2. Для работы скрипта нужен Python версии не ниже 3.7
3. Установите зависимости, указанные в файле ``requirements.txt`` командой:

   ```pip install -r requirements.txt```
4. Получите токен Девмана по [ссылке](https://dvmn.org/api/docs/)
5. Создайте бота для получения оповещений о результатах код-ревью (основной бот) и получите его токен, написав в Telegram [BotFather](https://telegram.me/BotFather)
6. Создайте бота для получения логов работы основного бота (лог-бот) и получите его токен, написав в Telegram [BotFather](https://telegram.me/BotFather)
7. Узнайте chat id, написав в Telegram [специальному боту](https://telegram.me/userinfobot)
8. Создайте в корне проекта файл ``.env`` и укажите в нем все вышеуказанные данные, по образцу:

```
DVMN_TOKEN=токен, полученный в п.4
BOT_TOKEN=токен, полученный в п.5
LOG_BOT_TOKEN=токен, полученный в п.6
CHAT_ID=chat id, полученный в п.7
```

## Как запустить

Скрипт запускается командой:

   ```python3 main.py```

## Результат работы 

Результатом работы бота будут сообщения о статусе код-ревью с сайта [dvmn.org](https://dvmn.org/):

В случае, если урок принят, в Telegram приходит сообщение: 

```
Вашу работу "{lesson_title}" проверили, преподаватель принял работу: {lesson_url}
```

В случае, если урок не принят, в Telegram приходит сообщение:

```
Вашу работу "{lesson_title}" проверили, преподаватель нашел ошибки: {lesson_url}
```
где 

```lesson_title``` - наименование проверенного урока,

```lesson_url``` - ссылка на проверенный урок.

При запуске основного бота, лог-бот пришлет сообщение: ``'Бот запущен'``

При возникновении ошибок в работе основного бота, лог-бот пришлет: ``Бот упал с ошибкой: {error}``, где ``error`` - наименование ошибки и её трейсбек.

## Чтобы развернуть скрипт в Docker-контейнере:

1. Устaновите Docker [Инструкция по установке](https://docs.docker.com/get-docker/)
2. Запустите bash и получите root-права командой:

```sudo -i``` 

3. Перейдите в папку проекта
4. Запустите сборку образа командой:

```docker build . -t bot```, 

где ``bot`` - наименование образа (можно использовать своё)

5. Запустите приложение в контейнере командой:

```
docker run --name tasks_check_bot -d -e DVMN_TOKEN='...' -e BOT_TOKEN='...' -e LOG_BOT_TOKEN='...' -e CHAT_ID='...' bot
```
где:
```
tasks_check_bot - наименование контейнера (можно использовать своё)
bot - наименование образа из п.4 настоящего Раздела
DVMN_TOKEN=токен, полученный в п.4 Раздела "Как установить"
BOT_TOKEN=токен, полученный в п.5 Раздела "Как установить"
LOG_BOT_TOKEN=токен, полученный в п.6 Раздела "Как установить"
CHAT_ID=chat id, полученный в п.7 Раздела "Как установить"

```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

## Автор проекта

Елена Иванова [Leeny_the_bear](https://github.com/leenythebear)


