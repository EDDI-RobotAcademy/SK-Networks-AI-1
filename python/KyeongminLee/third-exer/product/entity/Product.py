class Product:
    __productCd = None
    __autoIncrementProductCd = 0

    def __init__(self, productname):
        Product.__autoIncrementProductCd += 1
        self.__productCd = f'P{Product.__autoIncrementProductCd:03}'
        self.__productName = productname

    def getProductCd(self):
        return self.__productCd

    def getProductName(self):
        return self.__productName
