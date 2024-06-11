import { ActionContext } from "vuex"
import { Product, ProductState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"
import { REQUEST_PRODUCT_LIST_TO_DJANGO } from "./mutation-types"


export type ProductActions = {
    requestProductListToDjango(context: ActionContext<ProductState, any>): Promise<void>
    requestCreateProductToDjango(context: ActionContext<ProductState, unknown>, payload: {
        productName: string, writer: string, productPrice: number, productDescription: string
    }): Promise<AxiosResponse>
}

const actions: ProductActions = {
    async requestProductListToDjango(context: ActionContext<ProductState, any>): Promise<void> {
        try {
            const res: AxiosResponse<any, any> = await axiosInst.djangoAxiosInst.get('/product/list/');
            console.log('data:', res);
            const data: Product[] = res.data;
            console.log('data:', data)
            context.commit('REQUEST_PRODUCT_LIST_TO_DJANGO', data);
        } catch (error) {
            console.error('Error fetching product list:', error);
            throw error
        }
    },
    async requestCreateProductToDjango(context: ActionContext<ProductState, unknown>, payload: {
        productName: string, writer: string, productPrice: number, productDescription: string
    }): Promise<AxiosResponse> {

        console.log('requestCreateBoardToDjango()')

        const { productName, writer, productPrice, productDescription } = payload
        console.log('전송할 데이터:', { productName, writer, productPrice, productDescription })

        try {
            const res: AxiosResponse = await axiosInst.djangoAxiosInst.post(
                '/product/register', { productName, writer, productPrice, productDescription })

            console.log('res:', res.data)
            return res.data
        } catch (error) {
            alert('requestCreateProductToDjango() 문제 발생!')
            throw error
        }
    }
}

export default actions;