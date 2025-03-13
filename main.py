from fastapi import FastAPI
from app.core.database import create_db_and_tables
from app.routes import router

app = FastAPI(title="Solabs API", version="1.0")

app.include_router(router)

@app.on_event("startup")
def startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"message": "A API Solabs está rodando!"}