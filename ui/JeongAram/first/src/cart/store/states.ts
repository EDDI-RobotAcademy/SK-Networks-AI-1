export interface CartState {
    cartItemList: CartItem[];
}

export interface CartItem {
    productId: number;
    productName: string;
    produdctPrice: number;
    quantity: number;
}

const state: CartState = {
    cartItemList: [],
}

export default state