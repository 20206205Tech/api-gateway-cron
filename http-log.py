import json

import requests

# URL trực tiếp của API Gateway HTTP Log
url = "https://api-gateway-http-log.20206205.tech"

# Thiết lập headers (Mở comment và thêm token nếu API yêu cầu xác thực)
headers = {
    "Accept": "application/json",
    # "Authorization": "Bearer <TOKEN_CỦA_BẠN>"
}


def fetch_logs():
    try:
        # Thực hiện request GET
        print(f"Đang gọi API: {url}")
        response = requests.get(url, headers=headers)

        # Bắt lỗi HTTP Code (4xx, 5xx)
        response.raise_for_status()

        if response.text.strip():
            # Parse JSON và in ra màn hình
            data = response.json()
            formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
            print(formatted_json)
        else:
            print("API phản hồi thành công nhưng không có dữ liệu (Empty Response).")

    except requests.exceptions.HTTPError as http_err:
        print(f"Lỗi HTTP xảy ra: {http_err}")
        print("Chi tiết phản hồi lỗi:", response.text)
    except requests.exceptions.JSONDecodeError:
        print("Lỗi: Phản hồi trả về không phải định dạng JSON hợp lệ.")
        print("Nội dung thực tế:", response.text)
    except Exception as err:
        print(f"Đã xảy ra lỗi hệ thống: {err}")


if __name__ == "__main__":
    fetch_logs()
