# http-log.py
from api_client import fetch_and_print_api

url = "https://api-gateway-http-log.20206205.tech"
headers = {
    "Accept": "application/json",
}

if __name__ == "__main__":
    fetch_and_print_api(url, headers=headers)
