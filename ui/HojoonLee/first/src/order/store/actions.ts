import { ActionContext } from "vuex"
import { OrderItem, OrderState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type OrderActions = {
    requestCreateOrderToDjango(
        context: ActionContext<OrderState, any>,
        payload: {
            userToken: string;
            items: {
                cartItemId: number;
                quantity: number;
                orderPrice: number
            }[]
        }
    ): Promise<AxiosResponse>;
}

const actions: OrderActions = {
    // 이 함수는 cart에서 실행된 함수임
    async requestCreateOrderToDjango({ state }, payload) {
        try {
            const userToken = localStorage.getItem('userToken');
            if (!userToken) {
                throw new Error('User token not found');
            }

            console.log('payload:', payload)

            const requestData = {
                userToken,
                // map 옆에 있는 item은 payload.items에서 자동으로 뽑혀나온 애들을 의미 (lambda처럼) 
                // map(x => 했으면) 이후는 x.cartItemId, x.quantity 식으로 쓰면 됨
                items: payload.items.map(item => ({
                    cartItemId: item.cartItemId,
                    quantity: item.quantity,
                    orderPrice: item.orderPrice
                }))
            };

            const response =
                await axiosInst.djangoAxiosInst.post('/orders/create', requestData);
            console.log('response data:', response.data)

            return response.data;
        } catch (error) {
            console.error('Error creating order:', error);
            throw error;
        }
    }
};

export default actions;