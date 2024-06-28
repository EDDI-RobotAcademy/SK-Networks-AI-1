
export interface OrderState {
    orderList: OrderItem[];
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
}

export default state
