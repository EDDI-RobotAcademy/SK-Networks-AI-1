import { ActionContext } from "vuex"
import { Product, ProductState } from "./states"
import { AxiosResponse} from "axios"
import axiosInst from "@/utility/axiosInstance"
import { REQUEST_PRODUCT_LIST_TO_DJANGO, REQUEST_PRODUCT_TO_DJANGO } from "./mutation-types"


export type ProductActions = {
    requestProductToDjango(context: ActionContext<ProductState, any>, productId: number): Promise<void>
    requestProductListToDjango(context: ActionContext<ProductState, any>): Promise<void>
    requestCreateProductToDjango(context: ActionContext<ProductState, unknown>, imageFormData: FormData): Promise<AxiosResponse>
  
    requestDeleteProductToDjango(context: ActionContext<ProductState, unknown>, productId: number): Promise<void>
    // requestModifyProductToDjango(context: ActionContext<ProductState, any>, payload:{
    //     productName: string, productPrice: number, content: string, productId: number}): Promise<void>
}

const actions: ProductActions = {
    async requestProductToDjango(
        context: ActionContext<ProductState, any>, 
        productId: number): Promise<void> {
        try {
            const res: AxiosResponse<Product> = 
                await axiosInst.djangoAxiosInst.get(`/product/read/${productId}`)

            context.commit(REQUEST_PRODUCT_TO_DJANGO, res.data)
        } catch (error) {
            console.error('requestProductToDjango() -> error:', error)
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
    
    async requestCreateProductToDjango(context: ActionContext<ProductState, unknown>, imageFormData: FormData): Promise<AxiosResponse> {
        try {
                console.log('requestCreateProductToDjango()')
                const res: AxiosResponse = await axiosInst.djangoAxiosInst.post('/product/register', imageFormData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                console.log('응답 데이터 : ', res.data)
                alert('상품이 성공적으로 등록되었습니다.');
                return res
            } catch (error) {
                console.log('requestCreateProductToDjango(): ', error)
                throw error
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
    // async requestModifyProductToDjango(context: ActionContext<ProductState, any>, 
    //     payload:{ productName: string, productPrice: number, content: string, productId: number}): Promise<void> {
    //     const { productName, productPrice, content, productId} = payload
    //     try {
    //         await axiosInst.djangoAxiosInst.put(`/product/modify/${productId}`, {productName, productPrice, content})
    //         console.log('수정 성공!')
    //     } catch (error) {
    //         console.log('requestModifyProductToDjango() 과정에서 문제 발생')
    //         throw error
    //     }
    // }

}

export default actions;