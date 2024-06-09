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
    # 오히려 이건 get으로 하기보단 register로 하는게 좋음
    # 함수이름과 하는행위가 달라서 모호성을 줌
    # service_impl 함수 이름도 마찬가지!
    def getProductList(self):
        for i in ProductCode:
            self.__productlist.append(i)
        return self.__productlist
