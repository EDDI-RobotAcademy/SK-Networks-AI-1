from product.repository.product_repository_impl import ProductRepositoryImpl

class DomainInitializer:

    @staticmethod
    def initProductDomain():
        ProductRepositoryImpl.getInstance()


    @staticmethod
    def initEachDomain():
        DomainInitializer.initProductDomain()

        ### 인이셔라이저 호출함으로써, 생성