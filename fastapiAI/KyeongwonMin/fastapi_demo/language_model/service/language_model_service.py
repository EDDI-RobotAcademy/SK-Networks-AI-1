from abc import ABC, abstractmethod


class LanguageModelService(ABC):
    @abstractmethod
    def operateLanguageModel(self):
        pass

    @abstractmethod
    def predictWithModelingLanguage(self, userRequestForm):
        pass
