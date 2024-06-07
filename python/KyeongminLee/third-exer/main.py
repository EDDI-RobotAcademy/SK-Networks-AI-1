from product.entity.Product import Product
from initializer.domain_initializer import DomainInitializer
from product.service.product_service_impl import ProductServiceImpl

DomainInitializer.initEachDomain()
'''
[문제정의]
Product Domain을 만들어봅시다.
회원 없고, 상품 추가, 삭제 없이 상품 리스트 출력으로 진행하겠습니다!
'''
def keepProductDomainInstance():
    global productService
    productService = ProductServiceImpl.getInstance()

def keepDomainInstance():
    keepProductDomainInstance()

def createProduct(producntName):
    productService.createProduct(producntName)


if __name__ == "__main__":
    keepDomainInstance()

    productNames = ["아이패드", "아이폰", "애플워치"]
    createProduct(productNames)

    print(productService.getProductList())