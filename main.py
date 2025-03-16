import uvicorn
from fastapi import FastAPI
from nicegui import ui
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router
from app.database.db import create_db_and_tables
from dotenv import load_dotenv

from client.main import setup_pages

load_dotenv()

app = FastAPI(title="Solabs API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # Allow all origins (for development only!)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(router)

ui.run_with(app)

@app.on_event("startup")
def startup():
    create_db_and_tables()
    setup_pages()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

#MAS QUE MERDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA