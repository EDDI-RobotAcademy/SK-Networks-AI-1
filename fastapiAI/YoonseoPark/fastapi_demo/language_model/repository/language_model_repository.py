from abc import ABC, abstractmethod


class LanguageModelRepository(ABC):
    @abstractmethod
    def preprocessForCreateUniqueCharacter(self, text):
        pass

    @abstractmethod
    def preprocessForCreateTextIndex(self, text, charToIndex):
        pass

    @abstractmethod
    def createDataSet(self, text, textAsIndex):
        pass

    @abstractmethod
    def trainModel(self, sequenceList, characterList):
        pass