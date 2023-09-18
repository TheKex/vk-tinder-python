## Требования
* БД: postgress

Создать .env по аналогии с .env.example
```commandline
VK_BOT_TOKEN - ВК токен сообщества
VK_USER_TOKEN - ВК токен админа
DB_HOST - адресс БД (например 192.168.80.119)
DB_PORT - порт БД (например 5119)
DB_USER - пользователь БД (например postgres)
DB_PASS - пароль пользователя (12345qwerty)
DB_NAME - имя базы (например postgres)
```

Перед запуском, необходимо установить библиотеки из requirements.txt
```commandline
pip install -r requirements.txt
```

Бота запускать командой
```commandline
python bot.py
```
