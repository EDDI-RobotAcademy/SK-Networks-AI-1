import requests
import os


class HttpRequestInstance:
    base_url = os.getenv("AI_BASE_URL")

    @classmethod
    def post(cls, endpoint, data=None, headers=None):
        if not cls.base_url:
            raise ValueError("AI_BASE_URL is not set in .env file")

        url = f"{cls.base_url}{endpoint}"
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"HTTP Request failed: {e}")
            return None