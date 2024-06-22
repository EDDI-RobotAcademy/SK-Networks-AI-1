export interface CartState {
    cartItemList: CartItem[]
    cartItem: CartItem | null
}

export interface CartItem {
    productId: number
    productName: string
    productPrice: string
    quantity: number
}

const state: CartState = {
    cartItemList: [],
    cartItem: null,
}

export default state