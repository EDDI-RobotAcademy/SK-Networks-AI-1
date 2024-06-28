export interface CartState {
    cartItemList: CartItem[];
}

export interface CartItem {
    productId: number;
    productName: string;
    productPrice: number;
    quantity: number;
}

const state: CartState = {
    cartItemList: [],
}

export default state