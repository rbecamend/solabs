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
        lab_str += f"[{lab.laboratory_id}] {lab.name}: {lab.description}\n"
    for rsr in rsrs:
        rsr_str += f"{rsr.name} (lab_id: {rsr.laboratory_id}, email: {rsr.email})\n"

    #PROMPT = f"""Você é um orientador acadêmico da faculdade de computação da UFPA. Recomende um laboratório com base
    #no comentário do usuário: {valid_text}. Estes são os laboratórios existentes da FACOMP: {lab_str}. Quando tiver em mãos o/os
    #laboratórios recomendados, diga para o aluno procurar os professores relacionados a tal lab/labs: {rsr_str}.
    #"""

    # PROMPT = f"""
    # Você é um orientador acadêmico da Faculdade de Computação da UFPA. Um aluno escreveu o seguinte comentário: "{valid_text}"
    # Com base nisso, recomende **dois laboratórios mais compatíveis** com o perfil do aluno. Use as descrições dos laboratórios a seguir:
    # LABORATÓRIOS:
    # {lab_str}
    # Eis os professores vinculados aos respectivos laboratórios:
    # PROFESSORES:
    # {rsr_str}
    # Sua resposta deve seguir exatamente este formato:
    # dois laboratórios mais compatíveis com você:
    # - Lab 1: <nome do laboratório>
    # - Lab 2: <nome do laboratório>
    # por que?:
    # Explique brevemente por que esses dois laboratórios são os mais adequados.
    # professores que você pode tentar contatar:
    # Lab 1:
    # - <professor 1> = <email>
    # - <professor 2> = <email>
    # Lab 2:
    # - <professor 3> = <email>
    # - <professor 4>> = <email>
    # A resposta deve ser clara, organizada e direta.
    # """

    PROMPT = f"""
    Você é um orientador acadêmico da Faculdade de Computação da UFPA. Um aluno escreveu o seguinte comentário: "{valid_text}"

    Com base nesse comentário, recomende **exatamente dois laboratórios mais compatíveis** com o perfil do aluno.

    Aqui estão os laboratórios disponíveis:
    {lab_str}

    E aqui estão os professores, com seus respectivos laboratórios:
    {rsr_str}

    **Importante**:
    - Só recomende laboratórios que estejam na lista acima.
    - Ao listar os professores, **inclua apenas os que têm vínculo com os laboratórios recomendados**.
    - Mantenha a correspondência correta entre laboratórios e professores.

    Formato da resposta (siga exatamente este modelo):

    dois laboratórios mais compatíveis com você:
    - Lab 1: <nome do laboratório>
    - Lab 2: <nome do laboratório>

    por que?:
    Explique brevemente por que esses dois laboratórios são os mais adequados ao perfil do aluno.

    professores que você pode tentar contatar:
    Lab 1:
    - <professor 1> = <email>
    - <professor 2> = <email>

    Lab 2:
    - <professor 3> = <email>
    - <professor 4> = <email>

    A resposta deve ser clara, organizada e direta.
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
