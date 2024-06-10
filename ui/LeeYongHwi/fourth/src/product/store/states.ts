export interface ProductState {
    products: Product[]
    product: Product | null
}

export interface Product {
    productId: number
    productName: string
    price: number
}

const state: ProductState = {
    products: [],
    product: null
}

export default state