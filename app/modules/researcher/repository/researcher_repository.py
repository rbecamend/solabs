from sqlalchemy.orm import Session
from modules.researcher.model.researcher_model import ResearcherModel

class ResearcherRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_researchers(self):
        return self.db.query(ResearcherModel).all()