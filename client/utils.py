import json

TOKEN_FILE = "token.json"

def save_token(token: str) -> None:
    with open(TOKEN_FILE, "w", encoding="utf-8") as f:
        json.dump({"token": token}, f)

def get_token() -> str | None:
    try:
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("token")
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def clear_token() -> None:
    with open(TOKEN_FILE, "w", encoding="utf-8") as f:
        json.dump({}, f)