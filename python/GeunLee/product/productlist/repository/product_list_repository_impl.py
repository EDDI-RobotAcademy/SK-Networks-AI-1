from productlist.entity.product import Product
from productlist.repository.product_list_repository import ProductListRepository
from productlist.entity.productList import ProductList


class ProductListRepositoryImpl(ProductListRepository):
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
        self.__productList.clear()
        for product in ProductList:
            product_name, product_price = product.value
            self.__productList.append(Product(product_name, product_price))
        return self.__productList
