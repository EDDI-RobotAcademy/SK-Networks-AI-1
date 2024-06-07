from initializer.domain_initializer import DomainInitializer
from product.service.product_service_impl import ProductServiceImpl

DomainInitializer.initEachDomain()

if __name__ == "__main__":

    product_service = ProductServiceImpl.getInstance()

    product_service.displayProductList()
