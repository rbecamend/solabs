from nicegui import ui
import requests
from client.utils import get_token, clear_token

API_URL = "http://localhost:8000"

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

    response = requests.post(f"{API_URL}/labs/recommend", json={"preferences": user_input}, headers=headers)

    if response.status_code == 200:
        recommendations = response.json()
        result_label.set_text(f"Laboratórios recomendados:\n{recommendations}")
    else:
        ui.notify("Erro ao buscar recomendações!", type="negative")

def home_page():
    global text_area, result_label

    with ui.card():
        ui.label("Digite seus interesses acadêmicos:")
        text_area = ui.textarea(placeholder="Exemplo: Inteligência Artificial, Banco de Dados...")
        ui.button("Buscar Laboratórios", on_click=submit_preferences)
        result_label = ui.label("")
        ui.button("Sair", on_click=logout, color="red")
