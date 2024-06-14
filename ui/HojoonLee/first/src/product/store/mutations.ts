import { MutationTree } from "vuex";
import { ProductState, Product } from "./states";
import { 
    REQUEST_PRODUCT_LIST_TO_DJANGO 
} from "./mutation-types";

export interface ProductMutations extends MutationTree<ProductState> {
    [REQUEST_PRODUCT_LIST_TO_DJANGO] (state: ProductState, receivedData: Product[]): void
}

const mutations: MutationTree<ProductState> = {
    [REQUEST_PRODUCT_LIST_TO_DJANGO] (state: ProductState, receivedData: Product[]): void {
        state.productList = receivedData
    }
}

export default mutations as ProductMutations