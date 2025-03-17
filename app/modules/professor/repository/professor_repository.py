from sqlalchemy.orm import Session
from modules.professor.model.professor_model import ProfessorModel

class ProfessorRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_professors(self):
        return self.db.query(ProfessorModel).all()