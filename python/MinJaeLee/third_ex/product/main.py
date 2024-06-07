from initializer.domain_initializer import DomainInitializer
from product.service.product_service_impl import productServiceImpl

DomainInitializer.initEachDomain()

if __name__ == "__main__":
    productService = productServiceImpl.getInstance()
    productService.displayProductList()
