from service.product_service_impl import ProductServiceImpl
from initializer.domain_initializer import DomainInitializer

DomainInitializer.initEachDomain()

def makeProductDomainInstance():
    global productService
    productService = ProductServiceImpl.getInstance()

def createProduct(productname):
    productService.create(productname)

if __name__ == "__main__":
    makeProductDomainInstance()

    productName = "통크"
    createProduct(productName)

    productService.getProductList()
    print(product.getProductName())