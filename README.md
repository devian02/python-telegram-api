# Python Telegram API

🚧 Work in progress 🚧

This is a Python Library that helps you to use telegram APIs.

## The purpose

The purpose of the library is to facilitate the use of the telegram API with Python.

## 📘 The documentation
The following section contain all the useful information to use this library at its best. Read it carefully.

### Installation
You can use Python Telegram API directly from source code by cloning the repository from github.

```bash
git clone https://github.com/xSklero/python-telegram-api.git
```


❗ This library will be available on Pypi when completed. ❗

### Usage

```python

from python_telegram_api import telegram_bot_api

myBot = telegram_bot_api.TelegramBotApi('xxxxxxxxxx:yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')

print(myBot._getUpdates())

```

Use [BotFather](https://core.telegram.org/bots#6-botfather) to create your bot and your token.

You can use find more about this library in the wiki section: https://github.com/xSklero/python-telegram-api/wiki

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.