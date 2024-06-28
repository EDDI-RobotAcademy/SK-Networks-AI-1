import actions, { OrderActions } from "./actions"
import mutations, { OrderMutations } from "./mutations"
import state, { OrderState } from "./states"

export interface OrderModule {
    namespaced: true
    state: OrderState
    actions: OrderActions
    mutations: OrderMutations
}

const orderModule: OrderModule = {
    namespaced: true,
    state,
    actions,
    mutations,
}

export default orderModule