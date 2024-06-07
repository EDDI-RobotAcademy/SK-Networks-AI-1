from product.service.product_service_impl import ProductServiceImpl


def keepProductDomainInstance():
    global productService
    productService = ProductServiceImpl.getInstance()


def keepDomainInstance():
    keepProductDomainInstance()

def createProductList(productName):
    productService.createProductList(productName)


if __name__ == "__main__":

    keepDomainInstance()

    # -------- 상품 등록  --------
    firstProductName = "감자"
    createProductList(firstProductName)

    secondProductName = "고구마"
    createProductList(secondProductName)

    thirdProductName = "사과"
    createProductList(thirdProductName)

    # -------- 상품 리스트 출력  --------
    for product in productService.getProductList():
        print(f"상품 번호: {product.getProductId()}, 상품명: {product.getProductName()}")
