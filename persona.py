# persona.py
from api_client import fetch_and_print_api

url = "https://20206205.tech/api/api-gateway/code-persona-service/persona/public"
params = {"page": 1, "size": 50}

if __name__ == "__main__":
    fetch_and_print_api(url, params=params)
