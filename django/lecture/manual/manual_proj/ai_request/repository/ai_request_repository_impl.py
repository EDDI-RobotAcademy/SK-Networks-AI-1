from ai_request.repository.ai_request_repository import AiRequestRepository
from api.http_request import HttpRequestInstance


class AiRequestRepositoryImpl(AiRequestRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def aiRequest(self, userToken, command, data):
        endpoint = "/ai-request"

        payload = {
            "userToken": userToken,
            "command": command,
            "data": data
        }

        print(f"userToken: {userToken}, command: {command}, data: {data}")

        response = HttpRequestInstance.post(endpoint, data=payload)

        if response:
            print("AI Request Success:", response)
        else:
            print("AI Request Failed")

        return True

