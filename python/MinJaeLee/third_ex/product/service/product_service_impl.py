from product.repository.product_repository_impl import productRepositoryImpl
from product.service.product_service import productService


class productServiceImpl(productService):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__productRepository = productRepositoryImpl.getInstance()
            return cls.__instance
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def displayProductList(self):
        productList = self.__productRepository.getProductList()
        for product in productList:
            print(f"{product.value}번째 상품 : {product.name}")
