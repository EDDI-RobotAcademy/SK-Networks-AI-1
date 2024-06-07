from product.entity.product import Product
from product.repository.product_repository import ProductRepository

class ProductRepositoryImpl(ProductRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__fixedProductList = []
            # 2번 부르기, 그럼 객체 부를때 바로 2개 정보 append -> 근데 실제로 이렇겐 안할 듯.. 여기가 지저분
            # 단순히 생성자로 값을 설정하는 방식과 약간 다름
            # cls.__instance를 사용했고 싱글톤이라는 전제가 있어 사용가능한 방식
            # 싱글톤이 아니라면 객체마다 빈 list에서 다시 쌓이기 때문에 객체마다 서로 다른 정보를 가짐 (공유 x)
            cls.__instance.__fixedProductList.append(
                Product("상품1",500,"상품1은 500원입니다.")
            )
            cls.__instance.__fixedProductList.append(
                Product("상품2",1000,"상품2은 1000원입니다.")
            )
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def list(self):
        # 여기서 무언갈 보여줘야 하니까 보여줄 것을 __new__에서 만들어주자!
        # cls.__instance.__fixedProductList
        return self.__fixedProductList