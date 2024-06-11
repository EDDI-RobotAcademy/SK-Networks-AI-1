from abc import ABC, abstractmethod


class ProductRepository(ABC):

    @abstractmethod
    def create(self, product):
        pass

    @abstractmethod
    def find_by_id(self, product_id):
        pass

    @abstractmethod
    def update(self, product):
        pass

    @abstractmethod
    def delete_by_id(self, product_id):
        pass
