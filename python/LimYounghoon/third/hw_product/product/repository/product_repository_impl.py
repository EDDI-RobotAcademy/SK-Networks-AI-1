from product.entity.product import Product
from product.repository.product_repository import ProductRepository


class ProductRepositoryImpl(ProductRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__productList = []

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, productList):
        for productName in productList:
            product = Product(productName)
            self.__productList.append(product)

    def getProductList(self):
        return self.__productList

    def list(self):
        return self.__productList
