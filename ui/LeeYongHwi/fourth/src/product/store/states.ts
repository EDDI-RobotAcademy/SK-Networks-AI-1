export interface ProductState {
    products: Product[]
    product: Product | null
}

export interface Product {
    productId: number
    productName: string
    price: string
}

const state: ProductState = {
    products: [],
    product: null
}

export default state