import * as axiosUtility from "../../utility/axiosInstance"
import { aiRequestState } from "./aiRequestState";
import { useAiRequestStore } from "./aiRequestStore";

export const aiRequestActions = {
    async aiRequestToFastAPI() {
        const aiRequestStore = useAiRequestStore()

        const { fastapiAxiosInst } = axiosUtility.createAxiosInstances()

        try {
            const response = await fastapiAxiosInst.post('/ai-request')
            aiRequestStore.isRequestSuccessful = response.data
        } catch (error) {
            console.error('게시글 목록을 불러오는 중 에러가 발생했습니다:', error)
        }
    }
}