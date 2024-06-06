from initializer.domain_initializer import DomainInitializer
from product.service.product_service_impl import ProductServiceImpl


DomainInitializer.initEachDomain()

def keepProductDomainInstance():
    global productService
    productService = ProductServiceImpl.getInstance()

def keepDomainInstance():
    keepProductDomainInstance()

def createProduct(productName):
    productService.createProduct(productName)


if __name__ == "__main__":
    keepDomainInstance()

    firstProductName = "상품1"
    createProduct(firstProductName)

    secondproductName = "상품2"
    createProduct(secondproductName)

    for product in productService.getProductList():
        print(f"상품{product.getProdudctId()}: {product.getProductName()}")