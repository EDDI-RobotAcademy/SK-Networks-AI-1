from repository.product_repository import ProuductRepository
from entity.product import Product

class ProductRepositoryImpl(ProuductRepository):
    __instance =None

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

    def create(self,productname):
        product = Product(productname)
        self.__productList.append(product)

    def findProductByProductName(self, productname):
        for product in self.__productList:
            if product.getProductName() == productname:
                return product

    def getProductlist(self):
        return self.__productList
0

