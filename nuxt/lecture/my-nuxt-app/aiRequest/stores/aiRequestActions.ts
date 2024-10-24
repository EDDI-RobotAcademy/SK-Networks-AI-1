import * as axiosUtility from "../../utility/axiosInstance"
import { aiRequestState } from "./aiRequestState";
import { useAiRequestStore } from "./aiRequestStore";

export const aiRequestActions = {
    async aiRequestToDjango() {
        const aiRequestStore = useAiRequestStore()

        const { djangoAxiosInst } = axiosUtility.createAxiosInstances()

        const payload = {
            userToken: "test",
            command: 1,
            // data: [] 데이터 없을 경우도 있음
        };

        try {
            const response = await djangoAxiosInst.post('/ai-request/send', payload)
            aiRequestStore.isRequestSuccessful = response.data
        } catch (error) {
            console.error('게시글 목록을 불러오는 중 에러가 발생했습니다:', error)
        }
    }
}