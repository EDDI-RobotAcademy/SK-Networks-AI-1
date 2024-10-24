from ai_request.repository.ai_request_repository_impl import AiRequestRepositoryImpl
from ai_request.service.ai_request_service import AiRequestService
from backlog.repository.backlog_repository_impl import BacklogRepositoryImpl



class AiRequestServiceImpl(AiRequestService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__aiRequestRepository = AiRequestRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def aiRequestToFastAPI(self, userToken, data):
        try:
            return self.__aiRequestRepository.aiRequest(userToken, data)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e
