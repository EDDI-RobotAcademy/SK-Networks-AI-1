import actions, { OrderActions } from "./actions"
import state, { OrderState } from "./states"

export interface OrderModule {
    namespaced: true
    state: OrderState
    actions: OrderActions
}

const orderModule: OrderModule = {
    namespaced: true,
    state,
    actions
}

export default orderModule