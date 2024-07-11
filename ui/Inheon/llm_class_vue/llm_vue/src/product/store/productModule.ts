import actions, { ProductActions } from "./actions"
import mutations, { ProductMutations } from "./mutations"
import state, { ProductState } from "./states"

export interface ProductModule {
    namespaced: true
    state: ProductState
    actions: ProductActions
    mutations: ProductMutations
}

const productModule: ProductModule = {
    namespaced: true,
    state,
    actions,
    mutations,
}

export default productModule