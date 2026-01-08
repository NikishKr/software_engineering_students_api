from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api.endpoints import router


# Создание таблицы
Base.metadata.create_all(bind=engine)

# Создание экземпляра FastAPI
app = FastAPI()
app.include_router(router, prefix="/api/v1")

# Корневой эндпоинт API
@app.get("/")
def root():
    return {"message": "Students API"}