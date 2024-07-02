import actions, { CartActions } from "./actions"
// import mutations, {CartMutations} from "./mutations"
import state, { CartState } from "./states"

export interface CartModule {
    namespaced: true
    actions: CartActions
    state: CartState
    // mutations: CartMutations
}

const cartModule: CartModule = {
    namespaced: true,
    actions,
    state,
    // mutations // 나중에는 필요하다고 함
}

export default cartModule