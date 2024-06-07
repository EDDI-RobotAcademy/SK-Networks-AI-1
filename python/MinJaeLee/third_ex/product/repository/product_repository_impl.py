from product.entity.product_code import productCode
from product.repository.product_repository import productRepository


class productRepositoryImpl(productRepository):
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

    def getProductList(self):
        for product in productCode:
            self.__productList.append(product)
        return self.__productList