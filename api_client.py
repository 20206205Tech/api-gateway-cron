# api_client.py
import json

import requests


def fetch_and_print_api(url, headers=None, params=None):
    """Hàm dùng chung để gọi API và in kết quả JSON."""
    try:
        print(f"Đang gọi API: {url}")
        response = requests.get(url, headers=headers, params=params)

        # Kiểm tra nếu HTTP Status Code lỗi
        response.raise_for_status()

        # Kiểm tra nếu phản hồi có nội dung
        if response.text.strip():
            data = response.json()
            formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
            print(formatted_json)
        else:
            print("API phản hồi thành công nhưng nội dung trống (Empty Response).")

    except requests.exceptions.HTTPError as http_err:
        print(f"Lỗi HTTP xảy ra: {http_err}")
        print("Chi tiết phản hồi lỗi:", response.text)
    except requests.exceptions.JSONDecodeError:
        print("Lỗi: Phản hồi trả về không phải là định dạng JSON hợp lệ!")
        print("Nội dung thực tế nhận được:", response.text)
    except Exception as err:
        print(f"Đã xảy ra lỗi hệ thống: {err}")
