import requests

from modules.laboratory.service.laboratory_service import LaboratoryService
from modules.llm.dtos.text_input_dto import TextInputDTO
from modules.professor.service.professor_service import ProfessorService

def ask_llm(text: TextInputDTO, laboratory_service: LaboratoryService, professor_service: ProfessorService):
    labs = laboratory_service.get_all_laboratories()
    profs = professor_service.get_all_professors()
    lab_str = ""
    prof_str = ""
    for lab in labs:
        lab_str += f"lab_id: {lab.laboratory_id}, {lab.description}, {lab.name};"
    for prof in profs:
        prof_str += f"{prof.name}, lab_id: {prof.laboratory_id};"

    PROMPT = f"""Você é um orientador acadêmico da faculdade de computação da UFPA. Recomende um laboratório com base 
    no comentário do usuário: {text}. Estes são os laboratórios existentes da FACOMP: {lab_str}. Quando tiver em mãos o/os 
    laboratórios recomendados, diga para o aluno procurar os professores relacionados a tal lab/labs: {prof_str}.
    """
    response = requests.post(
        "http://ollama:11434/api/generate",
        json={
            "model": "llama3.2:latest",
            "prompt": PROMPT,
            "stream": False
        }
    )

    response_json = response.json()

    return response_json['response']
