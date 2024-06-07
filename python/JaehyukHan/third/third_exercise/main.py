from initializer.domain_initializer import DomainInitializer
from product.service.product_service_impl import ProductServiceImpl

DomainInitializer.initEachDomain()

if __name__ == '__main__':
    productService = ProductServiceImpl.getInstance()
    productService.getProductList()
    productService.displayProductList()