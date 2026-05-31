# plans.py
from api_client import fetch_and_print_api

url = "https://20206205.tech/api/api-gateway/code-payment-service/plans"
params = {"skip": 0, "limit": 10}

if __name__ == "__main__":
    fetch_and_print_api(url, params=params)
