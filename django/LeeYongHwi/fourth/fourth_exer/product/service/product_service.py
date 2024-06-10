from abc import ABC, abstractmethod


class ProductService(ABC):
    @abstractmethod
    def list(self):
        pass