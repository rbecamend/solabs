from sqlmodel import Session, select
from app.modules.student.model.student_model import Student

class StudentRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_student(self, student: Student):
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        return student

    def get_student_by_id(self, student_id: int):
        return self.session.get(Student, student_id)

    def update_student(self, student: Student):
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        return student

    def delete_student(self, student_id: int):
        student = self.get_student_by_id(student_id)
        if student:
            self.session.delete(student)
            self.session.commit()
        return student

    def existy_by_matricula(self, matricula: str):
        statement = select(Student).where(Student.matricula == matricula)
        return self.session.exec(statement).first() is not None