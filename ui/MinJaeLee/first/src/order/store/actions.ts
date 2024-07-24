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

    requestReadOrderToDjango(
        context: ActionContext<OrderState, any>,
        payload: {
            orderId: string
        }
    ): Promise<AxiosResponse>
}

const actions: OrderActions = {
    async requestCreateOrderToDjango({ state }, payload) {
        try {
            const userToken = localStorage.getItem('userToken');
            if (!userToken) {
                throw new Error('User token not found');
            }

            console.log('payload:', payload)

            const requestData = {
                userToken,
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
    },

    async requestReadOrderToDjango({ state }, payload) {
        try {
            const userToken = localStorage.getItem('userToken');
            if (!userToken) {
                throw new Error('User token not found');
            }

            const { orderId } = payload

            const requestData = {
                userToken,
            }

            const response =
                await axiosInst.djangoAxiosInst.post(`/orders/read/${orderId}`, requestData)
            console.log('data:', response.data)

            return response.data
        } catch (error) {
            console.error('주문 내역 요청 중 에러:', error)
            throw error
        }
    }
};

export default actions;