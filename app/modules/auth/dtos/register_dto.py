from pydantic import BaseModel

class RegisterDTO(BaseModel):
    email: str
    senha: str
    curso: str
    matricula: str
    nome: str