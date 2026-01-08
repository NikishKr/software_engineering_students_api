from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Student(Base):
    """
    Класс, представляющий модель студента.

    Содержит атрибуты:
    id студента
    имя
    возраст
    id группы
    """
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Или String(100)
    age = Column(Integer, nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=True)

    group = relationship("Group", back_populates="students")