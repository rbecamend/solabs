import uvicorn
from fastapi import FastAPI
from nicegui import ui
from app.routes import router
from app.database.db import create_db_and_tables
from dotenv import load_dotenv

from client.main import setup_pages

load_dotenv()

app = FastAPI(title="Solabs API", version="1.0")

app.include_router(router)

ui.run_with(app)

@app.on_event("startup")
def startup():
    create_db_and_tables()
    setup_pages()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

#MAS QUE MERDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA