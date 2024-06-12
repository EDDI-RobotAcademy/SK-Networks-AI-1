from product.entity.models import Product
from product.repository.product_repository import ProductRepository


class ProductRepositoryImpl(ProductRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        print(f"list() -> Product", Product)
        print(f"list() -> Product.objects", Product.objects)
        print(f"list() -> Product.objects.all()", Product.objects.all())

        productList = Product.objects.all()
        for product in productList:
            print(f"Product: {product}")
        # models.py가 실질적으로 Django 설정과 연결되어 있음
        # 이 부분에 정의된 게시물 객체가 Product에 해당함
        # 즉 DB에서 Product를 표현하는 테이블을 읽어서 그 전체를 반환하는 작업

        return Product.objects.all().order_by('regDate')

    def create(self, productData):
        # title, writer, content 내용을 토대로 Product 객체를 생성
        # 이 객체는 또한 models.py에 의해 구성된 객체로
        # save()를 수행하는 순간 DB에 기록됨
        product = Product(**productData)
        product.save()
        return product

    def findByProductId(self, productId):
        return Product.objects.get(productId=productId)
