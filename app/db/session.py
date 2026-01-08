from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import get_settings


# Создание экземпляра, содержащего настройки приложения
settings = get_settings()

# Инициализация движка, через который выполняются все запросы к БД
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=False
)

# Инициализация фабрики сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Функция для создания и управления сессией базы данных.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()