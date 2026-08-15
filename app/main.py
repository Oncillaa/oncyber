from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.v1.endpoints import auth, users, scanner, osint, cve, subdomain, steam
from app.core.database import engine, Base

# Создаём таблицы в БД (если их нет)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="oncyber",
    description="Unified security toolkit",
    version="2.0.0"
)

# Разрешаем CORS для всех источников (для разработки)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры
app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(scanner.router, prefix="/api/v1")
app.include_router(osint.router, prefix="/api/v1")
app.include_router(cve.router, prefix="/api/v1")
app.include_router(subdomain.router, prefix="/api/v1")
app.include_router(steam.router, prefix="/api/v1")

# Подключаем статику (фронтенд)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {"message": "oncyber is running. Documentation: /docs"}