from sqlalchemy.orm import Session
from app.models.student import Student


class StudentService:
    """
    Класс, описывающий функции для эндпоинтов,
    связанных со студентами.
    """
    @staticmethod
    def create_student(db: Session, student_data):
        db_student = Student(
            name=student_data.name,
            age=student_data.age,
            group_id=student_data.group_id
        )
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student

    @staticmethod
    def get_student(db: Session, student_id: int):
        return db.query(Student).filter(Student.id == student_id).first()

    @staticmethod
    def get_all_students(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Student).offset(skip).limit(limit).all()

    @staticmethod
    def delete_student(db: Session, student_id: int):
        student = db.query(Student).filter(Student.id == student_id).first()
        if student:
            db.delete(student)
            db.commit()
            return True
        return False