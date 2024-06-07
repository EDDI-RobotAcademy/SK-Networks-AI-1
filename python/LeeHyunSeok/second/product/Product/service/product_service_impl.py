from Product.repository.product_repository_impl import ProductRepositoryImpl
from Product.service.product_service import ProductService


class ProductServiceImpl(ProductService):
    __instance = None


    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__ProductRepository = ProductRepositoryImpl.getInstance()
        return cls.__instance



    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance


    def getProductList(self):
        self.productlist = self.__ProductRepository.getProductList()

        return self.productlist

    def displayProductList(self):
        displayList  = self.getProductList()
        for i in displayList:
            print(f"상품명 : {i.name}")
