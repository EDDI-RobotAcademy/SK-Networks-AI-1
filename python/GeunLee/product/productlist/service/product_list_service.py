from abc import ABC, abstractmethod


class ProductListService(ABC):
    @abstractmethod
    def getProductList(self):
        pass
