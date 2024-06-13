import { ActionContext } from "vuex"
import { Product, ProductState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type ProductActions = {
    requestProductToDjango(context: ActionContext<ProductState, any>, productId: number): Promise<void>
    requestProductListToDjango(context: ActionContext<ProductState, any>): Promise<void>
    requestCreateProductToDjango(context: ActionContext<ProductState, unknown>, payload: {
        productName: string, price: string
    }): Promise<AxiosResponse>
}

const actions: ProductActions = {
    async requestProductToDjango(context: ActionContext<ProductState, any>, productId: number): Promise<void> {
        try {
            const res: AxiosResponse<any, any> = await axiosInst.djangoAxiosInst.get(`/product/read/${productId}`);
            console.log('data:', res.data)
            context.commit('REQUEST_PRODUCT_TO_DJANGO', res.data);
        } catch (error) {
            console.error('requestProductToDjango() 문제 발생:', error);
            throw error
        }
    },
    async requestProductListToDjango(context: ActionContext<ProductState, any>): Promise<void> {
        try {
            const res: AxiosResponse<any, any> = await axiosInst.djangoAxiosInst.get('/product/list/');
            console.log('data:', res)
            const data: Product[] = res.data;
            console.log('data:', data)
            context.commit('REQUEST_PRODUCT_LIST_TO_DJANGO', data);
        } catch (error) {
            console.error('Error fetching product list:', error);
        
            throw error
        }
    },
    async requestCreateProductToDjango(context: ActionContext<ProductState, unknown>, payload: {
        productName: string, price: string
    }): Promise<AxiosResponse> {

        console.log('requestCreateProductToDjango()')

        const { productName, price } = payload
        console.log('전송할 데이터:', { productName, price })

        try {
            const res: AxiosResponse = await axiosInst.djangoAxiosInst.post(
                '/product/register', { productName, price })

            console.log('res:', res.data)
            return res.data
        } catch (error) {
            alert('requestCreateProductToDjango() 문제 발생!')
            throw error
        }
    }
}

export default actions;