export interface ProductState {
    productList: Product[]
    product: Product | null
}

export interface Product {
    productId: number
    productName: string
    productPrice: string
    productDescription: string
    registeredDate: string
    updatedDate: string
}

const state: ProductState = {
    productList: [],
    product: null,
}

export default state