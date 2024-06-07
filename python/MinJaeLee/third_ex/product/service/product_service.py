from abc import ABC, abstractmethod


class productService(ABC):
    @abstractmethod
    def displayProductList(self):
        pass