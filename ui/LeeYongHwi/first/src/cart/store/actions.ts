import { ActionContext } from "vuex"
import { CartItem, CartState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"
// import { REQUEST_CART_LIST_TO_DJANGO } from "./mutation-types"

export type CartActions = {
    requestAddToCartToDjango(
        context: ActionContext<CartState, any>,
        cartData: CartItem
    ): Promise<AxiosResponse>;
}

const actions: CartActions = {
    async requestAddToCartToDjango({ commit }, cartData: CartItem) {
        try {
            const userToken = localStorage.getItem('userToken')
            if (!userToken) {
                throw new Error('User token not found')
            }
            
            const requestData = {
                ...cartData,
                userToken,
            }

            console.log('requestData:', requestData)

            const response = await axiosInst.djangoAxiosInst.post('/cart/register', requestData)
            return response.data
        } catch (error) { 
            console.error('Error adding to cart:', error)
            throw error
        }
    },
}

export default actions