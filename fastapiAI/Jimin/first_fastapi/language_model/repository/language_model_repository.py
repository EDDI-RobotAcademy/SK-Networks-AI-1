from abc import ABC, abstractmethod

class LanguageModelRepository(ABC):
    @abstractmethod
    def preprocessForCertainUniqueCharacter(self, text):
        pass

    @abstractmethod
    def preprocessForCertainTextIndex(self, text, charToIndex):
        pass

    @abstractmethod
    def createDataSet(self, text, textAsIndex):
        pass

    @abstractmethod
    def trainModel(self, sequenceList, characterList):
        pass

    @abstractmethod
    def requestToReadShakespeareModel(self):
        pass

    @abstractmethod
    def convertTextToTensor(self, userInputText, charToIndex):
        pass

    @abstractmethod
    def generateText(self, loadedModel, inputTensor, indexToChar):
        pass