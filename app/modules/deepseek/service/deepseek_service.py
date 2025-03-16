from openai import OpenAI
from app.modules.laboratory.service.laboratory_service import LaboratoryService
from app.modules.laboratory.repository.laboratory_repository import LaboratoryRepository
import os

api_url = os.getenv("LLM_URL")
api_key = os.getenv("LLM_KEY")

client = OpenAI(api_key=api_key, base_url=api_url)


class DeepSeekService:

    def __init__(self, lab_service:LaboratoryService, lab_repository: LaboratoryRepository):
        self.lab_service = lab_service
        self.lab_repository = lab_repository


    def get_lab_recommendations(self, preferences: str):

        labs = self.lab_service.get_all_laboratories()

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": f"{labs}"},
                {"role": "user","content": f"Você é um orientador acadêmico da faculdade de computação da UFPA (FACOMP),"
                                           f" e irá recomendar um laboratório com base nas seguintes preferências do aluno: {preferences},"},
            ],
            stream=False
        )

        recommended_lab_name = response['choices'][0]['message']['content']

        recommended_lab = next((lab for lab in labs if lab.name in recommended_lab_name), None)

        if recommended_lab:
            self.lab_repository.increment_recommendation(recommended_lab.laboratory_id)

        return recommended_lab_name

