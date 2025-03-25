import uvicorn
import sqlalchemy

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from routes import router
from database.db import create_db_and_tables
from dotenv import load_dotenv

from modules.laboratory.service.laboratory_service import LaboratoryService


load_dotenv()

app = FastAPI(title="Solabs API", version="1.0")


app.include_router(router)


@app.on_event("startup")
def startup():
    try:
        labs = service.get_all_laboratories()
        if not labs:
            create_db_and_tables()
    except Exception as e:
        print("Error:", e)
    #is_created = False
    #while not is_created:
        #try:
            #is_created = create_db_and_tables()
        #except sqlalchemy.exc.OperationalError:
           #pass

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "detail": "Requisição inválida. Verifique os campos enviados. Certifique-se de preencher corretamente e com os tipos certos."
        },
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

