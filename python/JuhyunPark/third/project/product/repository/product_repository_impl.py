from product.repository.product_repository import ProductRepository
from product.entity.product_code import ProductCode


class ProductRepositoryImpl(ProductRepository):
    __instance = None      ### 싱글턴 패턴 선언, 이미 인스턴스가 생성되었는지 확인해줌.

    def __new__(cls):   ## 싱글턴 선언하면, 처음 실행하는 생성자, 특수메서드
        if cls.__instance is None: ##해당 클래스의 인스턴스가 이전에 생성되었는지 여부를 검사합니다. 첫 번째 인스턴스 생성 요청 시, __instance는 None입니다
            cls.__instance = super().__new__(cls)##부모 클래스의 __new__ 메서드를 호출하여 실제 인스턴스를 생성하고, cls.__instance에 할당
            cls.__instance.__productlist = [] #productlist를 빈 리스트로 초기화합니다. 이 변수는 모든 인스턴스에서 공유
        return  cls.__instance # 결국 productlist를 반환

    @classmethod  # 이 데코레이터는 메소드가 클래스 메소드임을 나타냄.
    def getInstance(cls):  #getInstance 메소드는 싱글톤 인스턴스를 얻기 위한 메소드.
        if cls.__instance is None:
            cls.__instance = cls()  #싱글톤 인스턴스 생성.

        return cls.__instance

    def getProductList(self):
        for i in ProductCode:
            self.__productlist.append(i)
        return self.__productlist