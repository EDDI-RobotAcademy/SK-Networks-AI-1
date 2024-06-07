from product.service.product_service import ProductService
from product.repository.product_repository_impl import ProductRepositoryImpl


class ProductServiceImpl(ProductService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__productRepository = ProductRepositoryImpl.getInstance()
            cls.__instance.__productList = []

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getProductList(self):
        self.__productList = self.__productRepository.getProductList()

    def displayProductList(self):
        for product in self.__productList:
            print(f"{product.value}번째 상품 : {product.name}")