# 🛡️ oncyber

Универсальный набор инструментов для кибербезопасности с бэкендом на FastAPI.

---

## 📌 Возможности

- 🔐 **JWT-авторизация** — регистрация и вход с токенами
- 📡 **Порт-сканер** — многопоточное сканирование TCP-портов
- 🔍 **OSINT** — поиск информации по email/username (GitHub, HaveIBeenPwned)
- 🐞 **CVE-сканер** — поиск уязвимостей через circl.lu
- 🌐 **Субдомены** — поиск поддоменов через hackertarget
- 🎮 **Steam-аналитика** — статистика профиля и достижения
- 📊 **История задач** — все сканирования сохраняются в SQLite
- 🌙 **Тёмная тема** — UI в стиле твоего Steam Analyzer

---

## 🚀 Быстрый старт

### 1. Клонируй репозиторий

```bash
git clone https://github.com/Oncillaa/oncyber.git
cd oncyber
```

###2. Создай виртуальное окружение
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

###3. Установи зависимости
bash
pip install -r requirements.txt

###4. Создай .env файл
env
SECRET_KEY=oncyber_secret_key_2026
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=sqlite:///./oncyber.db

###5. Запусти сервер
bash
uvicorn app.main:app --reload

###6. Открой в браузере
Фронтенд: http://127.0.0.1:8000/static/index.html

Swagger: http://127.0.0.1:8000/docs

📁 Структура проекта
text
oncyber/
├── app/
│   ├── api/            # Эндпоинты (auth, scan, osint, cve, subdomain, steam)
│   ├── core/           # База данных, безопасность, зависимости
│   ├── models/         # SQLAlchemy модели (User, ScanTask)
│   ├── schemas/        # Pydantic схемы
│   └── main.py         # Точка входа
├── static/
│   └── index.html      # Фронтенд с тёмной темой
├── requirements.txt
├── .env
└── README.md
🛠️ Технологии
Python 3.11+

FastAPI — бэкенд-фреймворк

SQLAlchemy — ORM для SQLite

JWT — авторизация (python-jose + passlib[bcrypt])

Docker — контейнеризация (опционально)

HTML + CSS + JS — фронтенд

🔗 API Эндпоинты
Метод	Эндпоинт	Описание
POST	/api/v1/auth/register	Регистрация
POST	/api/v1/auth/login	Вход (JWT)
GET	/api/v1/users/me	Профиль
POST	/api/v1/scan/ports	Сканирование портов
POST	/api/v1/osint/search	OSINT
POST	/api/v1/cve/search	CVE-сканер
POST	/api/v1/subdomain/find	Поиск субдоменов
POST	/api/v1/steam/stats	Steam-аналитика

