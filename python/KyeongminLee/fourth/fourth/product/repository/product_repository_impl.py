from product.repository.product_repository import ProductRepository
from product.entity.product import Product
class ProductRepositoryImpl(ProductRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            # 단순히 생성자로 값을 설정하는 방식과는 약간 다름
            # cls.__instance를 사용했고 싱글톤이라는 전제가 있어 사용 가능한 방식임
            # 만약 싱글톤이 아닌데 이런 형식으로 구성했더라도 코드가 동작하긴 하겠지만
            # 본인의 의도와는 다르게 흘러갈 수 있으므로 언제나 명시적인 코드를 작성하도록 노력해야함
            cls.__instance.__fixedProductList = []
            cls.__instance.__fixedProductList.append(
                Product("상품1", 500, "상품1은 500원입니다"))
            cls.__instance.__fixedProductList.append(
                Product("상품2", 1000, "상품2은 1000원입니다"))

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        return self.__fixedProductList