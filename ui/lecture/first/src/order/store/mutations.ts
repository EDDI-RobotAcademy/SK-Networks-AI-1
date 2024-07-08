import { MutationTree } from "vuex";
import { OrderState, OrderItem, Orders } from "./states";
import { 
    REQUEST_ORDER_TO_DJANGO,
    REQUEST_ORDER_LIST_TO_DJANGO, 
    SET_CURRENT_PAGE_NUMBER,
    SET_TOTAL_PAGE_NUMBER
} from "./mutation-types";

export interface OrderMutations extends MutationTree<OrderState> {
    [REQUEST_ORDER_TO_DJANGO] (state: OrderState, receivedData: OrderItem): void
    [REQUEST_ORDER_LIST_TO_DJANGO] (state: OrderState, receivedData: OrderItem[]): void
    [SET_CURRENT_PAGE_NUMBER] (state: OrderState, pageNumber: number): void
    [SET_TOTAL_PAGE_NUMBER] (state: OrderState, pageNumber: number): void
}

const mutations: MutationTree<OrderState> = {
    [REQUEST_ORDER_TO_DJANGO] (state: OrderState, receivedData: OrderItem): void {
        state.order = receivedData
    },
    [REQUEST_ORDER_LIST_TO_DJANGO] (state: OrderState, receivedData: Orders[]): void {
        state.orderList = receivedData
    },
    [SET_CURRENT_PAGE_NUMBER] (state: OrderState, pageNumber: number): void {
        state.currentPageNumber = pageNumber
    },
    [SET_TOTAL_PAGE_NUMBER] (state: OrderState, pageNumber: number): void {
        state.totalPageNumber = pageNumber
    }
}

export default mutations as OrderMutations