from modules.professor.repository.professor_repository import ProfessorRepository

class ProfessorService:
    def __init__(self, professor_repository: ProfessorRepository):
        self.professor_repository = professor_repository

    def get_all_professors(self):
        return self.professor_repository.get_all_professors()