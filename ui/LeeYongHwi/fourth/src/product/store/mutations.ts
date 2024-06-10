import { MutationTree } from "vuex";
import { Product, ProductState } from "./states";
import { REQUEST_PRODUCT_LIST_TO_DJANGO} from "./mutation-types";

export interface ProductMutations extends MutationTree<ProductState> {
    [REQUEST_PRODUCT_LIST_TO_DJANGO] (state: ProductState, receivedData: Product[]): void
}

const mutations: MutationTree<ProductState> = {
    [REQUEST_PRODUCT_LIST_TO_DJANGO] (state: ProductState, receivedData: Product[]): void { 
        state.products = receivedData
    }
}

export default mutations as ProductMutations