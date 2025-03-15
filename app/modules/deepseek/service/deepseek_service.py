from openai import OpenAI
from app.modules.laboratory.service.laboratory_service import LaboratoryService
import os

api_url = os.getenv("LLM_URL")
api_key = os.getenv("LLM_KEY")

client = OpenAI(api_key=api_key, base_url=api_url)


class DeepSeekService:

    def __init__(self, lab_servie:LaboratoryService ):
        self.lab_service = lab_servie


    def get_lab_recommendations(self, preferences: str):
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user",
                 "content": f"Recomende um laboratório com base nas seguintes preferências: {preferences}"},
            ],
            stream=False
        )

        recommended_labs = []
        for lab in self.lab_service.get_all_laboratories():
            if preferences.lower() in lab.description.lower():
                recommended_labs.append(lab)

        return recommended_labs
