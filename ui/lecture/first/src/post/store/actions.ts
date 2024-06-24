import { ActionContext } from "vuex"
import { Post, PostState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"
import { REQUEST_POST_LIST_TO_FASTAPI } from "./mutation-types"

export type PostActions = {
    requestPostListToFastapi(
        context: ActionContext<PostState, any>
    ): Promise<void>
}

const actions: PostActions = {
    async requestPostListToFastapi(
        context: ActionContext<PostState, any>
    ): Promise<void> {

        try {
            console.log('requestPostListToFastapi()')
            const res: AxiosResponse<any, any> = await axiosInst.fastapiAxiosInst.get('/post/list')
            const data: Post[] = res.data
            console.log('data:', data)
            context.commit(REQUEST_POST_LIST_TO_FASTAPI, data)
        } catch (error) {
            console.error('requestPostListToFastapi() 중 에러 발생:', error)
            throw error
        }
        
    }
};

export default actions;