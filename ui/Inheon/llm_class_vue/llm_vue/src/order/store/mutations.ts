import { MutationTree } from "vuex";
import { OrderState, OrderItem } from "./states";
import { 
    REQUEST_ORDER_TO_DJANGO,
    REQUEST_ORDER_LIST_TO_DJANGO 
} from "./mutation-types";

export interface OrderMutations extends MutationTree<OrderState> {
    [REQUEST_ORDER_TO_DJANGO] (state: OrderState, receivedData: OrderItem): void
    [REQUEST_ORDER_LIST_TO_DJANGO] (state: OrderState, receivedData: OrderItem[]): void
}

const mutations: MutationTree<OrderState> = {
    [REQUEST_ORDER_TO_DJANGO] (state: OrderState, receivedData: OrderItem): void {
        state.order = receivedData
    },
    [REQUEST_ORDER_LIST_TO_DJANGO] (state: OrderState, receivedData: OrderItem[]): void {
        state.orderList = receivedData
    }
}

export default mutations as OrderMutations