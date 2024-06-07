from abc import ABC, abstractmethod

class ProuductRepository(ABC):

    @abstractmethod
    def create(self,prouductname):
        pass

    @abstractmethod
    def findProductByProductName(self, productname):
        pass

    @abstractmethod
    def getProductlist(self):
        pass