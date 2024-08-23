from abc import abstractmethod, ABC


class LangchainService(ABC):
    @abstractmethod
    def ragWithLangChain(self, userSendMessage):
        pass