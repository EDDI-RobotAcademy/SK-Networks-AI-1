from product.service.product_service import ProductService
from product.repository.product_repository_impl import ProductRepositoryImpl


class ProductServiceImpl(ProductService):

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

    def list(self):
        return self.__ProductRepository.list()

    def createProduct(self, productData):
        self.__ProductRepository.create(productData)
