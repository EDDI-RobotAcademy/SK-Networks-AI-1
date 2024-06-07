from product.repository.product_repository import ProductRepository
from product.entity.product_code import ProductCode

class ProductRepositoryImpl(ProductRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__productlist = []
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getProductList(self):
        for i in ProductCode:
            self.__productlist.append(i)
        return self.__productlist
