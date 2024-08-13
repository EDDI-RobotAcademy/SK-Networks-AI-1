import { ActionContext } from "vuex"
import { AICommandState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"
import { REQUEST_AI_COMMAND_RESULT_TO_FASTAPI } from "./mutation-types"

export type AICommandActions = {
    requestAICommandToFastAPI(context: ActionContext<AICommandState, any>, aiCommandNumber: number): Promise<void>
    requestProcessedAICommandResultToFastAPI(context: ActionContext<AICommandState, any>): Promise<void>
}

const actions: AICommandActions = {
    async requestAICommandToFastAPI(context: ActionContext<AICommandState, any>, aiCommandNumber: number): Promise<void> {
        try {
            const res = await axiosInst.fastapiAxiosInst.post('/request-ai-command', {
                command: aiCommandNumber
            });
            console.log('data:', res.data)
        } catch (error) {
            console.error('requestAICommandToFastAPI() 문제 발생:', error);
            throw error
        }
    },
    async requestProcessedAICommandResultToFastAPI(context: ActionContext<AICommandState, any>): Promise<void> {
        try {
            const res: AxiosResponse<any, any> = await axiosInst.fastapiAxiosInst.post('/dice-result');
            console.log('data:', res)
            const data = res.data;
            console.log('data:', data)
            context.commit('REQUEST_AI_COMMAND_RESULT_TO_FASTAPI', data);
        } catch (error) {
            console.error('Error fetching AI Command Result:', error);
            throw error
        }
    },
};

export default actions;