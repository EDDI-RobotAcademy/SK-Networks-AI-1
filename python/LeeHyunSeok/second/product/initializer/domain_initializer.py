from Product.repository.product_repository_impl import ProductRepositoryImpl


class DomainInitializer:
    @staticmethod
    def initProductDomain():
        ProductRepositoryImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initProductDomain()