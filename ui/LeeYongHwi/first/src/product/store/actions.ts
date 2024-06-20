import { ActionContext } from "vuex"
import { Product, ProductState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type ProductActions = {
    requestProductListToDjango(context: ActionContext<ProductState, any>): Promise<void>
    requestCreateProductToDjango(context: ActionContext<ProductState, unknown>, 
                                imageFormData: FormData): Promise<AxiosResponse>
    requestProductToDjango(context: ActionContext<ProductState, any>, productId: number): Promise<void>
}

const actions: ProductActions = {
    async requestProductListToDjango(context: ActionContext<ProductState, any>): Promise<void> {
        try {
            const res: AxiosResponse<any, any> = await axiosInst.djangoAxiosInst.get('/product/list/');
            const data: Product[] = res.data;
            console.log('data:', data)
            context.commit('REQUEST_PRODUCT_LIST_TO_DJANGO', data);
        } catch (error) {
            console.error('Error fetching board list:', error);
            throw error
        }
    },
    async requestCreateProductToDjango(context: ActionContext<ProductState, unknown>, 
                                        imageFormData: FormData): Promise<AxiosResponse> {
        try {
            console.log('requestCreateBoardToDjango()')

            const res: AxiosResponse = await axiosInst.djangoAxiosInst.post(
                '/product/register', imageFormData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })

            console.log('응답 데이터:', res.data)
            return res
        } catch (error) {
            console.error('requestCreateProductToDjango():', error)
            throw error
        }
    },
    async requestProductToDjango(context: ActionContext<ProductState, any>, productId: number): Promise<void> {
        try {
            const res: AxiosResponse<Product> = await axiosInst.djangoAxiosInst.get(`/product/read/${productId}`)
            console.log('data:', res.data)
            context.commit('REQUEST_PRODUCT_TO_DJANGO', res.data);
        } catch (error) {
            console.error('requestProductToDjango() 문제 발생:', error);
            throw error
        }
    },
};

export default actions;