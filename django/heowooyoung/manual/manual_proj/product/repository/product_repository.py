from abc import abstractmethod, ABC

from product.entity.models import Product


class ProductRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, productName, productPrice, productDescription, productImage):
        pass

    @abstractmethod
    def findByProduct(self, productId):
        try:
            return Product.object.get(productId=productId)
        except Product.DoesNotExist:
            return None
