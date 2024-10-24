from abc import ABC, abstractmethod


class AiRequestService(ABC):
    @abstractmethod
    def aiRequestToFastAPI(self, userToken, data):
        pass

