from service.product_service_impl import ProductRepositoryImpl


class DomainInitializer:

    @staticmethod
    def initProductDomain():
        ProductRepositoryImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initProductDomain()

