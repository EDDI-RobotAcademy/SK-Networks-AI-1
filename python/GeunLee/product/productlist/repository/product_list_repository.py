from abc import ABC, abstractmethod


class ProductListRepository(ABC):
    @abstractmethod
    def getProductList(self):
        pass
