# main부터작성
from product.service.product_service import ProductService
from product.repository.product_repository import ProductRepository

def main():
    product_repository = ProductRepository()
    product_service = ProductService(product_repository)

    # 상품 추가
    product_service.add_product(1, '노트북', 1500)
    product_service.add_product(2, '스마트폰', 800)
    product_service.add_product(3, '태블릿', 600)

    #상품 리스트
    products = product_service.get_all_products()
    for product in products:
        print(product)

if __name__ == '__main__':
    main()
