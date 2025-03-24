from typing import List, Optional

from modules.laboratory.repository.laboratory_repository import LaboratoryRepository
from modules.laboratory.model.laboratory_model import LaboratoryModel
from modules.researcher.model.researcher_model import ResearcherModel


class LaboratoryService:
    def __init__(self, laboratory_repository: LaboratoryRepository):
        self.laboratory_repository = laboratory_repository

    def get_all_laboratories(self):
        return self.laboratory_repository.get_all_laboratories()

    def get_laboratory_by_id(self, laboratory_id: int):
        return self.laboratory_repository.get_laboratory_by_id(laboratory_id)

    def create_laboratory(self, name: str, description: str, professors: Optional[List[ResearcherModel]] = None):
        laboratory = LaboratoryModel(name=name, description=description, professors=professors or [])
        return self.laboratory_repository.create_laboratory(laboratory)

    def update_laboratory(self, laboratory_id: int, laboratory_data: dict):
        return self.laboratory_repository.update_laboratory(laboratory_id, laboratory_data)

    def delete_laboratory(self, laboratory_id: int):
        return self.laboratory_repository.delete_laboratory(laboratory_id)
