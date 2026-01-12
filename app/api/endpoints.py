from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.student import StudentCreate, StudentResponse
from app.schemas.group import GroupCreate, GroupResponse
from app.services.student_service import StudentService
from app.services.group_service import GroupService
from app.services.relationship_service import RelationshipService


# Создание экземпляра APIRouter
router = APIRouter()

# === Эндпоинты, связанные со студентами ===

# Эндпоинт для создания нового студента
@router.post("/students/", response_model=StudentResponse, status_code=201)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return StudentService.create_student(db, student)

# Эндпоинт для получения списка студентов
@router.get("/students/", response_model=List[StudentResponse])
def get_students(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return StudentService.get_all_students(db, skip, limit)

# Эндпоинт для получения информации о студенте по его id
@router.get("/students/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = StudentService.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")
    return student

# Эндпоинт для удаления студента
@router.delete("/students/{student_id}", status_code=204)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    if not StudentService.delete_student(db, student_id):
        raise HTTPException(status_code=404, detail="Студент не найден")

# === Эндпоинты, связанные с группами ===

# Эндпоинт для создания группы
@router.post("/groups/", response_model=GroupResponse, status_code=201)
def create_group(
    group: GroupCreate,
    db: Session = Depends(get_db)
):
    return GroupService.create_group(db, group)

# Эндпоинт для получения списка групп
@router.get("/groups/", response_model=List[GroupResponse])
def get_groups(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return GroupService.get_all_groups(db, skip, limit)

# Эндпоинт для получения информации о группе по её id
@router.get("/groups/{group_id}", response_model=GroupResponse)
def get_group(
    group_id: int,
    db: Session = Depends(get_db)
):
    group = GroupService.get_group(db, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Группа не найдена")
    return group

# Эндпоинт для удаления группы
@router.delete("/groups/{group_id}", status_code=204)
def delete_group(
    group_id: int,
    db: Session = Depends(get_db)
):
    if not GroupService.delete_group(db, group_id):
        raise HTTPException(status_code=404, detail="Группа не найдена")

# === Эндпоинты, связанные как со студентами, так и с группами ===

# Эндпоинт для добавления студента в группу
@router.post("/students/{student_id}/assign_group", response_model=StudentResponse)
def assign_student_to_group(
    student_id: int,
    group_id: int,
    db: Session = Depends(get_db)
):
    student, error = RelationshipService.assign_student_to_group(db, student_id, group_id)
    if error:
        raise HTTPException(status_code=404, detail=error)
    return student

# Эндпоинт для удаления студента из группы
@router.delete("/students/{student_id}/remove_group", response_model=StudentResponse)
def remove_student_from_group(
    student_id: int,
    db: Session = Depends(get_db)
):
    student, error = RelationshipService.remove_student_from_group(db, student_id)
    if error:
        raise HTTPException(status_code=404, detail=error)
    return student

# Эндпоинт для получения списка студентов в группе
@router.get("/groups/{group_id}/students", response_model=List[StudentResponse])
def get_students_in_group(
    group_id: int,
    db: Session = Depends(get_db)
):
    students = GroupService.get_students_in_group(db, group_id)
    if students is None:
        raise HTTPException(status_code=404, detail="Группа не найдена")
    return students

# Эндпоинт для перемещения студента из одной группы в другую
@router.put("/students/{student_id}/transfer", response_model=StudentResponse)
def transfer_student(
    student_id: int,
    new_group_id: int,
    db: Session = Depends(get_db)
):
    student, error = RelationshipService.transfer_student(db, student_id, new_group_id)
    if error:
        raise HTTPException(status_code=404, detail=error)
    return student