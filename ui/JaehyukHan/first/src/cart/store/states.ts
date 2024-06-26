export interface CartItem {
    productId: number;
    productName: string;
    productPrice: number;
    quantity: number;
}

export interface CartState {
    cartItemList: CartItem[];
}

const state: CartState = {
    cartItemList: [],
}

export default state