from abc import ABC, abstractmethod


class ProductService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create_product(self, product_data):
        pass

    @abstractmethod
    def read_product(self, product_id):
        pass

    @abstractmethod
    def update_product(slef, product_id):
        pass

    @abstractmethod
    def delete_product(self, product_id):
        pass
