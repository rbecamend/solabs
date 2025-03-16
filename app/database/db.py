from sqlmodel import create_engine, Session, SQLModel
from app.modules.student.model.student_model import StudentModel
from app.modules.auth.model.user_model import UserModel
from app.modules.professor.model.professor_model import ProfessorModel
from app.modules.laboratory.model.laboratory_model import LaboratoryModel
import os
from dotenv import load_dotenv

load_dotenv()

postgres_url = os.getenv("POSTGRES_URL")

engine = create_engine(postgres_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    engine.dispose()

def get_session():
    with Session(engine) as session:
        yield session

print(engine.url)