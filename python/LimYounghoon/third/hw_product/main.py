from product.service.product_service_impl import ProductServiceImpl
from initializer.product_initializer import DomainInitializer


DomainInitializer.initEachDomain()


def keepProductDomainInstance():
    global productService
    productService = ProductServiceImpl.getInstance()


def keepDomainInstance():
    keepProductDomainInstance()


def createProduct(productList):
    productService.createProduct(productList)


if __name__ == "__main__":
    keepDomainInstance()

    productShelves = [
        "맥북",
        "매직마우스",
        "매직트랙패드",
        "아이폰",
        "아이패드",
        "매직키보드",
    ]

    createProduct(productShelves)

    product_list = productService.getProductList()
    for product in product_list:
        print(f"상품명 : {product}")
