import actions, { ProductActions } from "./actions"
import mutations, { ProductMutations } from "./mutations"
import state, { ProductState } from "./states"

export interface ProductModule {
    // namespaced가 true가 되면 앞서 *.vue 코드에서 살펴봤듯이
    // 아래와 같은 문법이 허용됩니다.
    // const productModule = 'productModule'
    // ...mapState(productModule, ['products']),
    // 즉 productModule 자체를 위와 같이 참조할 수 있다는 의미입니다.
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