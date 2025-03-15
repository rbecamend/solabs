from pydantic import BaseModel

class LoginDTO(BaseModel):
    email: str
    senha: str