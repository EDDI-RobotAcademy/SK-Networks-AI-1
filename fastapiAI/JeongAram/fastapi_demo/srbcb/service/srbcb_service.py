from abc import ABC, abstractmethod

class SrbcbService(ABC):
    @abstractmethod
    def ruleBaseResponse(self, userSendMessage):
        pass
