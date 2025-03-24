from modules.researcher.repository.researcher_repository import ResearcherRepository

class ResearcherService:
    def __init__(self, professor_repository: ResearcherRepository):
        self.researcher_repository = professor_repository

    def get_all_researchers(self):
        return self.researcher_repository.get_all_researchers()