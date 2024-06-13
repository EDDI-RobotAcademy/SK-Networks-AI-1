export interface ProductState {
    products: Product[]
    product: Product | null
}

export interface Product {
    productId: number
    productName: string
    writer: string
    productDescription: string
    productPrice: number
    regDate: string
    updDate: string
}

const state: ProductState = {
    products: [],
    product: null
}

export default state