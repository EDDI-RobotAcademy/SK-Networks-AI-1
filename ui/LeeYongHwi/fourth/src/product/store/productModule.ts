import state, { ProductState } from "./states"
import mutations, { ProductMutations } from "./mutations"
import actions, {ProductActions} from "./actions"

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