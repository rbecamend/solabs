from sqlalchemy.orm import Session
from modules.laboratory.model.laboratory_model import LaboratoryModel

class LaboratoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_laboratories(self):
        return self.db.query(LaboratoryModel).all()

    def get_laboratory_by_id(self, laboratory_id: int):
        return self.db.query(LaboratoryModel).filter(LaboratoryModel.laboratory_id == laboratory_id).first()

    def create_laboratory(self, laboratory: LaboratoryModel):
        self.db.add(laboratory)
        self.db.commit()
        self.db.refresh(laboratory)
        return laboratory

    def update_laboratory(self, laboratory_id: int, laboratory_data: dict):
        laboratory = self.get_laboratory_by_id(laboratory_id)
        if laboratory:
            for key, value in laboratory_data.items():
                setattr(laboratory, key, value)
            self.db.commit()
            self.db.refresh(laboratory)
        return laboratory

    def delete_laboratory(self, laboratory_id: int):
        laboratory = self.get_laboratory_by_id(laboratory_id)
        if laboratory:
            self.db.delete(laboratory)
            self.db.commit()
        return laboratory
