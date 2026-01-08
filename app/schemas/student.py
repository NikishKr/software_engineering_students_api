from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


# Базовые атрибуты студента
class StudentBase(BaseModel):
    name: str
    age: int = Field(ge=0, le=120)
    group_id: Optional[int] = None


# Создание нового студента
class StudentCreate(StudentBase):
    pass


# Обновление значений атрибутов студента
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = Field(default=None, ge=0, le=120)
    group_id: Optional[int] = None


# Присвоение студенту идентификатора
class StudentResponse(StudentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)