import requests

from modules.laboratory.service.laboratory_service import LaboratoryService
from modules.llm.dtos.text_input_dto import TextInputDTO
from modules.researcher.service.professor_service import ResearcherService

class InvalidTextException(Exception):
    pass

def validate_text_input(text):
    user_text = text.text
    #if not isinstance(user_text, str):
        #raise InvalidTextException("O texto deve ser uma string.")
    if user_text.strip() == "":
        raise InvalidTextException("O texto não pode estar em branco ou conter apenas espaços.")
    if len(user_text.strip()) > 400:
        raise InvalidTextException("O texto é muito grande. Envie um conteúdo de até 400 caracteres.")
    if len(user_text.strip()) < 30:
        raise InvalidTextException("O texto deve ser maior que 30 caracteres, pense um pouco mais.")
    return user_text.strip()

def ask_llm(text: TextInputDTO, laboratory_service: LaboratoryService, researcher_service: ResearcherService):
    valid_text = validate_text_input(text)
    labs = laboratory_service.get_all_laboratories()
    rsrs = researcher_service.get_all_researchers()
    lab_str = ""
    rsr_str = ""
    for lab in labs:
        lab_str += f"lab_id: {lab.laboratory_id}, {lab.description}, {lab.name};"
    for rsr in rsrs:
        rsr_str += f"{rsr.name}, lab_id: {rsr.laboratory_id};"

    PROMPT = f"""Você é um orientador acadêmico da faculdade de computação da UFPA. Recomende um laboratório com base 
    no comentário do usuário: {valid_text}. Estes são os laboratórios existentes da FACOMP: {lab_str}. Quando tiver em mãos o/os 
    laboratórios recomendados, diga para o aluno procurar os professores relacionados a tal lab/labs: {rsr_str}.
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
