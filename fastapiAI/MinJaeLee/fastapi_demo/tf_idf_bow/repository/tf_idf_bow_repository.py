from abc import abstractmethod, ABC


class TfIdfBowRepository(ABC):
    @abstractmethod
    def findSimilar(self, message, countVectorizer, countMatrix):
        pass

    @abstractmethod
    def documentVectorization(self):
        pass
