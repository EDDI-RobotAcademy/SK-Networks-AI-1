import { ActionContext } from "vuex"
import { Product, ProductState } from "./states"
import { AxiosResponse, AxiosError } from "axios"
import axiosInst from "@/utility/axiosInstance"
import { REQUEST_PRODUCT_LIST_TO_DJANGO, REQUEST_PRODUCT_TO_DJANGO } from "./mutation-types"
import ProductRoutes from '@/product/router/ProductRoutes'


export type ProductActions = {
    requestProductToDjango(context: ActionContext<ProductState, any>, productId: number): Promise<void>
    requestProductListToDjango(context: ActionContext<ProductState, any>): Promise<void>
    requestCreateProductToDjango(context: ActionContext<ProductState, unknown>, payload: {
        prodname: string, price: number, writer: string, content: string }): Promise<AxiosResponse>
    requestDeleteProductToDjango(context: ActionContext<ProductState, unknown>, productId: number): Promise<void>
    requestModifyProductToDjango(context: ActionContext<ProductState, any>, payload:{
        prodname: string, price: number, content: string, productId: number}): Promise<void>
}

const actions: ProductActions = {
    async requestProductToDjango(context: ActionContext<ProductState, any>, productId: number): Promise<void>{
        try {
            const res: AxiosResponse<Product> = await axiosInst.djangoAxiosInst.get(`/product/read/${productId}`);
            console.log('data:',res.data)
            context.commit(REQUEST_PRODUCT_TO_DJANGO, res.data);
        } catch (error) {
            console.error('requestProductToDjango() 문제 발생:', error);
            throw error
        }
    },
    async requestProductListToDjango(context: ActionContext<ProductState, any>): Promise<void> {
        try {
            const res: AxiosResponse<any, any> = await axiosInst.djangoAxiosInst.get('/product/list/');
            console.log('res:',res)
            const data: Product[] = res.data;
            console.log('data:', data)
            context.commit(REQUEST_PRODUCT_LIST_TO_DJANGO, data);
        } catch (error) {
            console.error('Error fetching product list:', error);
            // 에러를 처리할 수 있는 추가 로직
            throw error
        }
    },
    
    async requestCreateProductToDjango(context: ActionContext<ProductState, unknown>, payload: {
        prodname: string, price: number, writer: string, content: string}): Promise<AxiosResponse> {
            console.log('requestCreateProductToDjango()')
            const { prodname, price, writer, content } = payload
            console.log('전송할 데이터:', { prodname, price, writer, content })
        
            try {
                const res: AxiosResponse = await axiosInst.djangoAxiosInst.post('/product/register', { prodname, price, writer, content})
                console.log('res:', res.data)
                alert('상품이 성공적으로 등록되었습니다.');
        
                return res.data
        
            } catch (error) {
                alert('requestCreateProductToDjango() 문제 발생!')
                throw error
                // if (error instanceof AxiosError) {
                //     alert('값을 모두 채우고, 가격은 숫자를 입력해주세요.')
                //     // ProductRoutes.push({ name: 'ProductListPage' })
                // } else {
                //     alert('requestCreateProductToDjango() 문제 발생!')
                //     throw error
                // }
            }
    },
    
    async requestDeleteProductToDjango(context: ActionContext<ProductState, unknown>, productId: number): Promise<void> {
        try{
            console.log('requestDeleteProductToDjango() ')
            // HTTP 상으로 DELETE 요청을 전송함
            await axiosInst.djangoAxiosInst.delete(`/product/delete/${productId}`)
        } catch (error) {
            console.log('requestDeleteProductToDjango() 과정에서 문제 발생!')
            throw error
        }
    },
    async requestModifyProductToDjango(context: ActionContext<ProductState, any>, 
        payload:{ prodname: string, price: number, content: string, productId: number}): Promise<void> {
        const { prodname, price, content, productId} = payload
        try {
            await axiosInst.djangoAxiosInst.put(`/product/modify/${productId}`, {prodname, price, content})
            console.log('수정 성공!')
        } catch (error) {
            console.log('requestModifyProductToDjango() 과정에서 문제 발생')
            throw error
        }
    }

};

export default actions;