import os

from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import text

from sqlmodel import create_engine, Session, SQLModel

load_dotenv()

postgres_url = os.getenv("POSTGRES_URL", "postgresql://postgres:postgres@postgres:5432/solabs_db")
engine = create_engine(postgres_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    engine.dispose()
    sql = text(Path("database/seed.sql").read_text())
    with Session(engine) as session:
        session.exec(sql)
        session.commit()

    return True

def get_session():
    with Session(engine) as session:
        yield session
