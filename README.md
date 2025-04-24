# 🗨️ Flask Chat App

Простой веб-чат, созданный на Flask, с возможностью регистрации, авторизации и личной переписки между пользователями.

## 🚀 Возможности

- 🔐 Регистрация и вход пользователей
- 💬 Отправка сообщений другим зарегистрированным пользователям
- 🧾 Список всех пользователей
- 📄 Чат в виде диалогов (1 на 1)
- 🧱 Backend на Flask
- 🖥️ Простые HTML-шаблоны на Jinja2


## ⚙️ Установка и запуск

1. Клонируй репозиторий:

```bash
git clone git@github.com:Shahzod2555/Chat.git
cd Chat
```

2. Создай виртуальное окружение и активируй его:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Установи зависимости:

```bash
pip install -r requirements.txt
```

4. Запусти приложение:

```bash
flask run
```

Открой в браузере `http://127.0.0.1:6969`

## 🧩 Структура проекта

```
src/
├── app.py           # Точка входа
├── ext.py           # Инициализация Flask расширений
├── model.py         # Модели пользователей и сообщений
├── router.py        # Роутинг
├── soc.py           # Чат-система
├── templates/       # HTML-шаблоны
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── users.html
│   └── chat.html
```

## 🛠️ Зависимости

- Flask
- Flask-SQLAlchemy (или другая ORM, если используешь)
- Flask-SocketIO
- Flask-Login
- Jinja2
- Python 3.8+

## 👨‍💻 Автор

**Shahzod Ergashev**  
[GitHub](https://github.com/Shahzod2555)

