from abc import abstractmethod, ABC


class ProductService(ABC):
    @abstractmethod
    def list(self):
        pass
    