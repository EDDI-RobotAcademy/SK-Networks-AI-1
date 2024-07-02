export interface CartState {
    cartItemList: CartItem[];
}

export interface CartItem {
    productId: number;
    prodName: string;
    price: number;
    quantity: number;
}

const state: CartState = {
    cartItemList: [],
}

export default state