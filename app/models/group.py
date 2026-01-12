from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base


class Group(Base):
    """
    Класс, представляющий модель группы.

    Содержит атрибуты:
    id
    название
    """
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    students = relationship("Student", back_populates="group")