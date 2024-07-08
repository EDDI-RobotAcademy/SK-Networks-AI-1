import { GetterTree } from "vuex";
import { Orders, OrderState } from "./states";

export interface OrderGetters extends GetterTree<OrderState, any> {
    orderList (state: OrderState): Orders[]
    currentPageNumber (state: OrderState): number
    totalPageNumber (state: OrderState): number
}

const getters: OrderGetters = {
    orderList: (state: OrderState) => state.orderList,
    currentPageNumber: (state: OrderState) => state.currentPageNumber,
    totalPageNumber: (state: OrderState) => state.totalPageNumber,
}

export default getters