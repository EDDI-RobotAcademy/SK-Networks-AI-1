import { MutationTree } from "vuex";
import { ProductState, Product } from "./states";
import { 
    REQUEST_PRODUCT_TO_DJANGO,
    REQUEST_PRODUCT_LIST_TO_DJANGO 
} from "./mutation-types";

export interface ProductMutations extends MutationTree<ProductState> {
    [REQUEST_PRODUCT_TO_DJANGO] (state: ProductState, receivedData: Product): void
    [REQUEST_PRODUCT_LIST_TO_DJANGO] (state: ProductState, receivedData: Product[]): void
}

const mutations: MutationTree<ProductState> = {
    [REQUEST_PRODUCT_TO_DJANGO] (state: ProductState, receivedData: Product): void {
        state.product = receivedData
    },
    [REQUEST_PRODUCT_LIST_TO_DJANGO] (state: ProductState, receivedData: Product[]): void {
        state.products = receivedData
    }
}

// 현재 Product Domain 만 다루고 있기 때문에 사실 아래와 같은 작업이 필요 없음
// 그러나 앞으로 추가할 것들을 고려한다면 예약어인 mutations를 피해야합니다.
// 고로 as를 사용하여 Product Domain 전용 Mutations라는 것을 표기하였습니다.
export default mutations as ProductMutations