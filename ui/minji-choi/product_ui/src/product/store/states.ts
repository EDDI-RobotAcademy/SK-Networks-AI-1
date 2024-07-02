export interface ProductState {
    // 대표적인 예이기도 함
    // products는 복수형이므로 배열 타입 (리스트를 의미하고 있음)
    // '변수: 타입' 형태로 표기함
    products: Product[]
    product: Product | null
}

// TypeScript는 특이한 형식이 있습니다.
// 어떤 형식이냐 ? python을 할 때 제일 불편했던 것은 무엇인가요 ?
// TypeScript에서는 다시 타입을 명시하게 됩니다.
export interface Product {
    productId: number
    productName: string
    productPrice: number
    writer: string
    content: string
    productCategory: string
    productImage: string
    regDate: string
    updDate: string
}

// 좋은 점도 있지만 단점이 있습니다.
// 뭐냐 ? 너무 엄격하다.
// 너무 엄격하다 못해 컴파일이 안됨
const state: ProductState = {
    products: [],
    product: null
}

export default state