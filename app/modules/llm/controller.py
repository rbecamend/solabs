import requests

from fastapi import APIRouter


router = APIRouter()


@router.post("/ask-llm")
def ask_llm(about_you: str):
    response = requests.post(
        "http://ollama:11434/api/generate",
        json={
            "model": "llama3.2:latest",
            "prompt": about_you,
            "stream": False
        }
    )

    print(response.json())