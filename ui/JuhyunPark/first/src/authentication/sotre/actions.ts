import { ActionContext } from "vuex"
import { AuthenticationState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"
import { REQUEST_BOARD_LIST_TO_DJANGO } from "./mutation-types"

export type BoardActions = {
    requestBoardToDjango(context: ActionContext<BoardState, any>, boardId: number): Promise<void>
    requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void>
    requestCreateBoardToDjango(context: ActionContext<BoardState, unknown>, payload: {
        title: string, writer: string, content: string
    }): Promise<AxiosResponse>
    requestDeleteBoardToDjango(context: ActionContext<BoardState, unknown>, boardId: number): Promise<void>
    requestModifyBoardToDjango(context: ActionContext<BoardState, any>, payload: {
        title: string, content: string, boardId: number
    }): Promise<void>
}

const actions: ProductActions = {
    async requestKakaoOauthRedirectionTodjango(): Promise<void> {
        return axiosInst.djangoAxiosInst.get('/oauth/kakao').then(res) => {
            console.log('requestKakaoOauthRedirectionTodjango() -> res:',
                        res.data.url)
            window.location.href = res.data.url
        })
    }
    return
};

export default actions;