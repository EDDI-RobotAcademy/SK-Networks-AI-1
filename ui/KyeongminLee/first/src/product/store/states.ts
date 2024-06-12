export interface ProductState {
    productList: Product[]
}

export interface Product {
    productId: number
    productName: string
    productPrice: string
    productDescription: string
    productImage: string
    registeredDate: string
    updatedDate: string
}

const state: ProductState = {
    productList: [],
}

export default state