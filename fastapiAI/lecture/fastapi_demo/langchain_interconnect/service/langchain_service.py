from abc import ABC, abstractmethod


class LangchainService(ABC):
    @abstractmethod
    def ragWithLangChain(self, userSendMessage):
        pass
