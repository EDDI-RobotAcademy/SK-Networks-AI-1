import actions, { CartActions } from "./actions"
import state, { CartState } from "./states"

export interface CartModule {
    namespaced: true
    state: CartState
    actions: CartActions
}

const cartModule: CartModule = {
    namespaced: true,
    state,
    actions
}

export default cartModule