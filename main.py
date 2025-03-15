from fastapi import FastAPI
from app.routes import router
from app.database.db import create_db_and_tables
app = FastAPI(title="Solabs API", version="1.0")
app.include_router(router)

@app.on_event("startup")
def startup():
    create_db_and_tables()
