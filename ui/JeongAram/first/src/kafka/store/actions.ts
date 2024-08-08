import { ActionContext } from "vuex"
import { kafkaTestItem, KafkaTestState } from "./states"
import axiosInst from "@/utility/axiosInstance"

export type KafkaTestActions = {
    requestKafkaTestDataToFastapi(
        context: ActionContext<KafkaTestState, any>,
        requestData: { message: string }
    ): Promise<any>
}

const actions: KafkaTestActions = {
    async requestKafkaTestDataToFastapi( 
        context: ActionContext<KafkaTestState, any>,
        requestData: { message: string }
    ): Promise<any> {

        try {
            const res =
                await axiosInst.fastapiAxiosInst.post(`/kafka-endpoint`, requestData);

            context.commit('REQUEST_KAFKA_TEST_DATA_TO_FASTAPI', true)
            return res
        } catch (error) {
            console.error('requestKafkaTestDataToFastapi() 문제 발생:', error)
            throw error
        }
    }
}

export default actions;