import requests
import os

def get_laboratory_recommendations(preferences: str) -> list:
    api_url = os.getenv("DEEPSEEK_API_URL")
    payload = {"preferences": preferences}
    headers = {"Content-Type": "application/json"}

    response = requests.post(api_url, json=payload, headers=headers)
    response.raise_for_status()

    return response.json().get("recommendations", [])