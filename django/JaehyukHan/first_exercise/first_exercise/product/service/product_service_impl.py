from product.service.product_service import ProductService
from product.repository.product_repository_impl import ProductRepositoryImpl


class ProductServiceImpl(ProductService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__productRepository = ProductRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createProduct(self, productData):
        self.__productRepository.create(productData)

    def list(self):
        return self.__productRepository.list()

    def readProduct(self, productId):
        return self.__productRepository.findByProductId(productId)





