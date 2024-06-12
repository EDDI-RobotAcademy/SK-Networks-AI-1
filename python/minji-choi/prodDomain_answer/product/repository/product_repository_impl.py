import random
from product.entity.product import Product
from product.repository.product_repository import ProductRepository
class ProductRepositoryImpl(ProductRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            # 단순히 생성자로 값을 설정하는 방식과는 약간 다름
            # cls.__instance를 사용했고, 싱글톤이라는 전제가 있어 사용한 방식
            # 싱글톤이 아니었다면 이런 형식으로 구성하면 코드는 동작하지만, 다른 위치에서 해당 객체는 이 객체가 아니게 됨
            cls.__instance.__fixedProductList = []
            cls.__instance.__fixedProductList.append(Product("상품1", 500, '상품1은 500원입니다.'))
            cls.__instance.__fixedProductList.append(Product("상품2", 1000, '상품2은 1000원입니다.'))
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def list(self):
        return self.__fixedProductList

