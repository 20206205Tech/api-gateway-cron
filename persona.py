import json

import requests

# URL API của bạn
url = "https://20206205.tech/api/api-gateway/code-persona-service/persona/public?page=1&size=50"

try:
    # Thực hiện request GET
    response = requests.get(url)

    # Kiểm tra nếu HTTP Status Code lỗi (4xx, 5xx) thì sẽ nhảy vào khối except
    response.raise_for_status()

    # Kiểm tra nếu phản hồi có nội dung
    if response.text.strip():
        # Chuyển response thành dữ liệu json (dict/list trong Python)
        data = response.json()

        # Format JSON với thụt lề 4 khoảng trắng và hỗ trợ tiếng Việt
        formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
        print(formatted_json)
    else:
        print("API phản hồi thành công nhưng nội dung trống (Empty Response).")

except requests.exceptions.HTTPError as http_err:
    print(f"Lỗi HTTP xảy ra: {http_err}")
    print("Nội dung phản hồi lỗi:", response.text)
except requests.exceptions.JSONDecodeError:
    print("Lỗi: Phản hồi trả về không phải là định dạng JSON hợp lệ!")
    print("Nội dung thực tế nhận được:", response.text)
except Exception as err:
    print(f"Đã xảy ra lỗi khác: {err}")
