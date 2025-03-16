import uvicorn
from fastapi import FastAPI

from routes import router
from database.db import create_db_and_tables
from dotenv import load_dotenv


load_dotenv()

app = FastAPI(title="Solabs API", version="1.0")

app.include_router(router)


@app.on_event("startup")
def startup():
    create_db_and_tables()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

