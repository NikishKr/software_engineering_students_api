from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from .student import StudentResponse


# Базовый атрибут группы
class GroupBase(BaseModel):
    name: str


# Создание новой группы
class GroupCreate(GroupBase):
    pass


# Обновление значения атрибута группы
class GroupUpdate(BaseModel):
    name: Optional[str] = None


# Присвоение группе идентификатора и списка студентов
class GroupResponse(GroupBase):
    id: int
    students: List[StudentResponse] = []

    model_config = ConfigDict(from_attributes=True)