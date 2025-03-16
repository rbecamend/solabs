import os

from dotenv import load_dotenv

from sqlmodel import create_engine, Session, SQLModel

load_dotenv()

postgres_url = os.getenv("POSTGRES_URL")
engine = create_engine(postgres_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    engine.dispose()

def get_session():
    with Session(engine) as session:
        yield session
