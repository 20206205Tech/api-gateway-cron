import json

import requests

url = "https://20206205.tech/api/api-gateway/code-persona-service/persona/public?page=1&size=50"

response = requests.request("GET", url)

# Chuyển response thành dữ liệu json (dict/list trong Python)
data = response.json()

# Format JSON với thụt lề 4 khoảng trắng và hỗ trợ chữ tiếng Việt (ensure_ascii=False)
formatted_json = json.dumps(data, indent=4, ensure_ascii=False)

print(formatted_json)
