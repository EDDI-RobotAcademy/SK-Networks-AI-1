

class DomainInitializer:
    @staticmethod
    def initProductDomain():
        ProductServiceImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initProductDomain()
