from product.repository.product_repository_impl import ProductRepositoryImpl
from product.service.product_service import ProductService


class ProductServiceImpl(ProductService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__ProductRepository = ProductRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createProduct(self, prod):
        self.__ProductRepository.create(prod)

    def getProductList(self):
        self.__ProductRepository.getProductList()