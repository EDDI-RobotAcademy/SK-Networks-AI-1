from product.entity.Product import Product
from product.repository.product_repository import ProductRepository


class ProductRepositoryImpl(ProductRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__productList = []

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, productNames):
        for name in productNames:
            product = Product(name)
            self.__productList.append(product)

    def list(self):
        return [f'{c.getProductCd()}-{c.getProductName()}' for c in self.__productList]

