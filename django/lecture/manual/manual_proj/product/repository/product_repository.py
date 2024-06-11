from abc import abstractmethod, ABC


class ProductRepository(ABC):
    @abstractmethod
    def list(self):
        pass
