import { ActionContext } from "vuex";
import {Post, PostState} from "./states"
import { AxiosResponse } from "axios";
import axiosInst from "@/utility/axiosInstance"
import {REQUEST_POST_LIST_TO_FASTAPI, REQUEST_POST_TO_FASTAPI} from "./mutation-types"

export type PostActions = {
    requestPostListToFastapi(context: ActionContext<PostState, any>)
    : Promise<void>,
    requestCreatePostToFastapi(context: ActionContext<PostState, unknown>,
        payload: {title: string, content: string}
    ): Promise<number>,
    requestPostToFastapi(context: ActionContext<PostState, any>,
        id: number
    ): Promise<void>
}

const actions: PostActions = {
    async requestPostListToFastapi(context: ActionContext<PostState, any>)
    : Promise<void> {
        try {
            const res: AxiosResponse<any, any> = await axiosInst.fastapiAxiosInst.get('/post/list')
            const data: Post[] = res.data
            console.log('data: ', data)
            context.commit(REQUEST_POST_LIST_TO_FASTAPI, data) // web상에 커밋
        } catch (error) {
            console.error('requestPostListToFastapi() 중 에러 발생', error)
            throw error
        }
    },
    async requestCreatePostToFastapi(context: ActionContext<PostState, unknown>,
        payload: {title: string, content: string}
        ): Promise<number> {
            const {title, content} = payload
            try {
                const res = await axiosInst.fastapiAxiosInst.post(
                    '/post/create', {title, content})
                console.log('res: ', res.data)
                return res.data.id
            } catch (error) {
                console.error('requestCreatePostToFastapi() 중 에러 발생 :', error)
                throw error
            }
    },
    async requestPostToFastapi(context: ActionContext<PostState, any>,
        id: number
    ): Promise<void> {
        try {
            const res: AxiosResponse<Post> = await axiosInst.fastapiAxiosInst.get(`/post/read/${id}`)
            console.log('read data :', res.data)
            context.commit(REQUEST_POST_TO_FASTAPI, res.data)
        } catch (error) {
            console.error('requestPostToFastapi() 중 에러 발생 :', error)
            throw error
        }
    }
}

export default actions