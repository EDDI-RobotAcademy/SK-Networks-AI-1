import { ActionContext } from "vuex"
import { Product, ProductState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type ProductActions = {
    requestProductListToDjango(context: ActionContext<ProductState, any>): Promise<void>
}

const actions: ProductActions = {
    async requestProductListToDjango(context: ActionContext<ProductState, any>): Promise<void> {
        try {
            const res: AxiosResponse<any, any> = await axiosInst.djangoAxiosInst.get('/product/list/');
            console.log('data:', res)
            const data: Product[] = res.data;
            console.log('data:', data)
            context.commit('REQUEST_Product_LIST_TO_DJANGO', data);
        } catch (error) {
            console.error('Error fetching product list:', error);
            // 에러를 처리할 수 있는 추가 로직
            throw error
        }
    },
}

export default actions;