from product.repository.product_repository_impl import ProductRepositoryImpl
from product.service.product_service import ProductService


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

    def list(self):
        print('서비스 list')
        return self.__productRepository.list()


    def createProduct(self, productName, productPrice, writer, productCategory, content, productImage):
        return self.__productRepository.create(productName, productPrice, writer, productCategory, content, productImage)


    def readProduct(self, productId):
        return self.__productRepository.findByProductId(productId)

    def removeProduct(self, productId):
        return self.__productRepository.deleteByProductId(productId=productId)

    def updateProduct(self, productId, productData):
        product = self.__productRepository.findByProductId(productId=productId)
        return self.__productRepository.update(product, productData)