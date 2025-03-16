from nicegui import ui
import requests
from client.utils import get_token, clear_token
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")

def logout():
    clear_token()
    ui.notify("Logout realizado!", type="info")
    ui.navigate.to("/login")

def submit_preferences():
    user_input = text_area.value.strip()
    if not user_input:
        ui.notify("Digite seus interesses!", type="warning")
        return

    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.post(f"{API_URL}/lab_recommendation", json={"text": user_input}, headers=headers)
        print(f"Resposta da API: {response.status_code}, {response.text}")

        if response.status_code == 200:
            recommendations = response.json()
            result_label.set_text(f"Laboratórios recomendados:\n{recommendations}")
        else:
            ui.notify(f"Erro ao buscar recomendações: {response.text}", type="negative")

    except Exception as e:
        print(f"Erro na requisição: {e}")
        ui.notify("Erro ao conectar ao servidor!", type="negative")

def home_page():
    global text_area, result_label

    with ui.card():
        ui.label("Digite seus interesses acadêmicos:")
        text_area = ui.textarea(placeholder="Exemplo: Inteligência Artificial, Banco de Dados...")
        ui.button("Buscar Laboratórios", on_click=submit_preferences)
        result_label = ui.label("")
        ui.button("Sair", on_click=logout, color="red")
