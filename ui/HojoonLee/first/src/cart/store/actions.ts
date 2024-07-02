import { ActionContext } from "vuex"
import {CartItem, CartState} from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"
import { REQUEST_CART_LIST_TO_DJANGO } from "./mutation-types"

export type CartActions = {
    requestAddCartToDjango(
        context: ActionContext<CartState, any>,
        cartData: CartItem
    ): Promise<AxiosResponse>;

    requestCartListToDjango(
        context: ActionContext<CartState, any>
    ): Promise<AxiosResponse>;
}

const actions: CartActions = {
    async requestAddCartToDjango({ commit }, cartData: CartItem) {
        try {
            // 상품등록은 누구건지 알아야하므로 userToken이 필요
            const userToken = localStorage.getItem('userToken');
            if (!userToken) {
                throw new Error('User token not found');
            }

            const requestData = {
                // ... : spread 기능 검색해보기
                ...cartData,
                userToken
            };

            console.log('requestData:', requestData);

            const response = await axiosInst.djangoAxiosInst.post('/cart/register', requestData);
            return response.data;
        } catch (error) {
            console.error('Error adding to cart:', error);
            throw error;
        }
    },

    async requestCartListToDjango({ commit }) {
        try {
            const userToken = localStorage.getItem('userToken');
            if (!userToken) {
                throw new Error('User token not found');
            }
            // 나와 관련된 정보만 list로 보여줘니까 userToken이 입력으로 필요
            const requestData = {
                userToken
            };

            console.log('requestCartListToDjango requestData:', requestData);

            const response = await axiosInst.djangoAxiosInst.post('/cart/list', requestData);
            return response.data;
        } catch (error) {
            console.error('Error fetching cart list:', error);
            throw error;
        }
    },
};

export default actions;