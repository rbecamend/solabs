from requests import session
from sqlmodel import Session, select
from modules.student.model.student_model import StudentModel

class StudentRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_student(self, student: StudentModel):
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        return student

    def get_student_by_id(self, student_id: int):
        return self.session.get(StudentModel, student_id)

    def update_student(self, student: StudentModel):
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

    def get_student_by_registration(self,registrations:str)->StudentModel:
        statement = select(StudentModel).where(StudentModel.registration == registrations)
        return self.session.exec(statement).first()
