export interface ProductState {
    productList: Product[]
}


//DB에 들어갈 필드를 정의(entity와 같은 역할인듯)
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
}

export default state