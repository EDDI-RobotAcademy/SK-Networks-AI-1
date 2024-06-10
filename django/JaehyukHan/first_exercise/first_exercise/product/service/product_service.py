from abc import ABC, abstractmethod

class ProductService(ABC):
    @abstractmethod
    def func1(self):
        pass