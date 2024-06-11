from abc import abstractmethod, ABC


class ProductRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, productData):
        pass
