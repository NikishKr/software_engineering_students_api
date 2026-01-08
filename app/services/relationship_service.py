from sqlalchemy.orm import Session
from app.models.student import Student
from app.models.group import Group


class RelationshipService:
    """
    Класс, описывающий функции для эндпоинтов,
    связанных со взаимодействием студентов и групп.
    """
    @staticmethod
    def assign_student_to_group(db: Session, student_id: int, group_id: int):
        student = db.query(Student).filter(Student.id == student_id).first()
        group = db.query(Group).filter(Group.id == group_id).first()

        if not student:
            return None, "Студент не найден"
        if not group:
            return None, "Группа не найдена"

        student.group_id = group_id
        db.commit()
        db.refresh(student)

        return student, None

    @staticmethod
    def remove_student_from_group(db: Session, student_id: int):
        student = db.query(Student).filter(Student.id == student_id).first()

        if not student:
            return None, "Студент не найден"

        student.group_id = None
        db.commit()
        db.refresh(student)

        return student, None

    @staticmethod
    def transfer_student(db: Session, student_id: int, new_group_id: int):
        student = db.query(Student).filter(Student.id == student_id).first()
        new_group = db.query(Group).filter(Group.id == new_group_id).first()

        if not student:
            return None, "Студент не найден"
        if not new_group:
            return None, "Новая группа не найдена"

        student.group_id = new_group_id
        db.commit()
        db.refresh(student)

        return student, None