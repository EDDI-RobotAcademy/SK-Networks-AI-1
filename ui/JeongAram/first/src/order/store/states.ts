export interface OrderState {
    orderList: OrderItem[];
    order: null
//     loading: boolean;
//     error: string | null;
}

export interface OrderItem {
    orderId: number;
    cartItemId: number;
    quantity: number;
    price: number;
}

const state: OrderState = {
    orderList: [],
    order: null
}

export default state