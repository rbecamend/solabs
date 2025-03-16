from nicegui import ui
import requests
from client.utils import save_token
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")

def login():
    email = email_input.value.strip()
    senha = senha_input.value.strip()

    if not email or not senha:
        ui.notify("Preencha todos os campos.", type="warning")
        return
    response = requests.post(f"{API_URL}/auth/login", json={"email": email, "password": senha})

    if response.status_code == 200:
        token = response.json().get("access_token")
        save_token(token)
        ui.notify("Login realizado com sucesso!", type="positive")
        ui.navigate.to("/home")
    else:
        ui.notify("Falha no login. Verifique suas credenciais.", type="negative")


def register():
    nome = nome_input.value.strip()
    matricula = matricula_input.value.strip()
    email = email_reg_input.value.strip()
    senha = senha_reg_input.value.strip()

    if not nome or not matricula or not email or not senha:
        ui.notify("Preencha todos os campos!", type="warning")
        return

    response = requests.post(f"{API_URL}/auth/register", json={
        "registration": matricula,
        "email": email,
        "password": senha
    })

    if response.status_code == 200:
        ui.notify("Cadastro realizado com sucesso. Faça login.", type="positive")
        ui.navigate.to("/login")
    else:
        ui.notify("Erro no cadastro. Verifique as informações.", type="negative")


def login_page():
    global email_input, senha_input

    with ui.card():
        ui.label("Login").classes("text-h5")
        email_input = ui.input("E-mail")
        senha_input = ui.input("Senha", password=True)
        ui.button("Entrar", on_click=login)
        ui.button("Registrar-se", on_click=lambda: ui.navigate.to("/register"))


def register_page():
    global nome_input, matricula_input, email_reg_input, senha_reg_input

    with ui.card():
        ui.label("Registro").classes("text-h5")
        nome_input = ui.input("Nome Completo")
        matricula_input = ui.input("Matrícula")
        email_reg_input = ui.input("E-mail")
        senha_reg_input = ui.input("Senha", password=True)
        ui.button("Registrar", on_click=register)
        ui.button("Já tem conta? Faça login", on_click=lambda: ui.navigate.to("/login"))
