from abc import ABC, abstractmethod


class GDFTService(ABC):
    @abstractmethod
    def gdftTest(self):
        pass

    @abstractmethod
    def gdftUserRequestTest(self, text):
        pass
