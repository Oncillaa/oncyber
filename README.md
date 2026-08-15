<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-0.109.0-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

<h1 align="center">🛡️ oncyber</h1>
<p align="center"><b>Универсальный набор инструментов для кибербезопасности</b><br>FastAPI + JWT + Тёмная тема</p>

---

## 📌 О проекте

**oncyber** — это единая платформа, которая объединяет твои любимые инструменты для пентеста и OSINT в одном месте. Всё работает через API и красивый веб-интерфейс с тёмной темой.

**Зачем это нужно?**
- Не нужно открывать 5 разных утилит — всё в одном окне
- Авторизация через JWT — данные каждого пользователя изолированы
- Все результаты сохраняются в базу данных
- Можно запускать сканирование и получать результат через пару секунд
- Готово для развёртывания на VPS или в Docker

---

## 🚀 Быстрый старт за 1 минуту

### 1. Склонируй репозиторий

```bash
git clone https://github.com/Oncillaa/oncyber.git
cd oncyber
```

### 2. Создай и активируй виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3. Установи зависимости

```bash
pip install -r requirements.txt
```

### 4. Создай файл `.env`

```bash
echo SECRET_KEY=supersecretkey > .env
echo ALGORITHM=HS256 >> .env
echo ACCESS_TOKEN_EXPIRE_MINUTES=60 >> .env
echo DATABASE_URL=sqlite:///./oncyber.db >> .env
```

### 5. Запусти сервер

```bash
uvicorn app.main:app --reload
```

### 6. Открой в браузере

| Ссылка | Что это |
|--------|---------|
| `http://127.0.0.1:8000/static/index.html` | 🌐 **Фронтенд** — красивая панель управления |
| `http://127.0.0.1:8000/docs` | 📖 **Swagger** — документация API |

---

## 🧠 Как это работает

```mermaid
flowchart LR
    A[Фронтенд<br>HTML+CSS+JS] -->|Запросы| B[FastAPI<br>Бэкенд]
    B -->|JWT-проверка| C[Авторизация]
    B -->|Запуск задач| D[Порт-сканер]
    B -->|Запросы к API| E[OSINT / CVE / Subdomain / Steam]
    B -->|Сохранение| F[(SQLite<br>База данных)]
```

---

## 🛠️ Доступные инструменты

| Инструмент | Что делает | Эндпоинт |
|------------|------------|----------|
| 📡 **Порт-сканер** | Сканирует TCP-порты на IP или домене | `POST /api/v1/scan/ports` |
| 🔍 **OSINT** | Ищет информацию по email/username | `POST /api/v1/osint/search` |
| 🛡️ **CVE Scanner** | Находит уязвимости по названию ПО | `POST /api/v1/cve/search` |
| 🌐 **Subdomain Finder** | Находит поддомены домена | `POST /api/v1/subdomain/find` |
| 🎮 **Steam Stats** | Показывает статистику Steam-профиля | `POST /api/v1/steam/stats` |

---

## 🔐 Авторизация

Все защищённые эндпоинты требуют **JWT-токен**.

| Эндпоинт | Метод | Что делает |
|----------|-------|------------|
| `/api/v1/auth/register` | POST | Регистрация |
| `/api/v1/auth/login` | POST | Получение токена |
| `/api/v1/users/me` | GET | Информация о пользователе |

**Пример запроса с токеном:**

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/scan/" \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..."
```

---

## 📁 Структура проекта

```
oncyber/
├── app/
│   ├── api/               # Эндпоинты
│   │   └── v1/endpoints/  # OSINT, CVE, Subdomain, Steam, Scanner
│   ├── core/              # База данных, безопасность
│   ├── models/            # SQLAlchemy-модели
│   ├── schemas/           # Pydantic-схемы
│   └── main.py            # Точка входа
├── static/
│   └── index.html         # Фронтенд с тёмной темой
├── requirements.txt
├── Dockerfile             # Готово для Docker
├── docker-compose.yml     # Готово для Compose
└── .env                   # Секретные настройки
```

---

## 🐳 Docker (опционально)

Если хочешь запустить проект одной командой:

```bash
docker-compose up --build
```

---

## 🎨 Тёмная тема

Фронтенд выполнен в твоём любимом стиле:

- Фон: `#0d1117` и `#1a1f26`
- Акцент: `#4f8cc9`
- Успех: `#7dd87d`
- Ошибка: `#f05050`
- Плавные анимации и скругления

---

## 📦 Технологии

| Технология | Для чего |
|------------|----------|
| **Python 3.11+** | Язык программирования |
| **FastAPI** | Веб-фреймворк |
| **SQLAlchemy** | ORM для базы данных |
| **SQLite** | База данных (можно сменить на PostgreSQL) |
| **JWT** | Авторизация |
| **Docker** | Контейнеризация |
| **HTML + CSS + JS** | Фронтенд |

---

## 📄 Лицензия

MIT © 2026 [Oncillaa](https://github.com/Oncillaa)

---

<p align="center">
  <a href="https://github.com/Oncillaa/oncyber">⭐ Поставь звезду</a>
  ·
  <a href="https://github.com/Oncillaa/oncyber/issues">🐛 Сообщить об ошибке</a>
</p>
