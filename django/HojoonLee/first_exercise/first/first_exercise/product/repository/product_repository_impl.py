from product.repository.product_repository import ProductRepository
from product.entity.models import Product


class ProductRepositoryImpl(ProductRepository):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super.__new__(cls)
            cls.__instance.__ProductRepository = ProductRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, productData):
        product = Product(**productData)
        product.save()
        return product
