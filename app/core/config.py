from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """
    Класс для настроек приложения, параметры
    загружаются из переменных окружения.
    """
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432

    @property
    def DATABASE_URL(self) -> str:
        """
        Формирует URL для подключения к базе данных PostgreSQL.

        Использует атрибуты класса для создания строки подключения.
        """
        return f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }


@lru_cache
def get_settings() -> Settings:
    """
    Возвращает экземпляр класса настроек.
    """
    return Settings()