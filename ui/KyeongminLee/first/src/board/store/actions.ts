import { ActionContext } from "vuex"
import { BoardState } from "./state"
import { AxiosResponse } from "axios"
import axios

export type BoardActions = {
    requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void>
}

// async와 Promise는 비동기 통신을 사용하기 위해 반드시 필요합니다
// 비동기 통신과 스레드, 병렬 처리, 앞서 살펴봤던 process.env가 모두 연관되어 있습니다
// 그래서 이 부분과 관련한 내용은 아마도 금요일 하루 종일 설명
// 이론이 매우 빡센 부분
// https://www.notion.so/eddi-robot-academy/thread-89c983d487ea4008998f1faeef6e2401
const actions: BoardActions = {
    async requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void> {
        try {
            const res: AxiosResponse<any, any> = 
                await axiosInt.djangoAxiosInst.get('/board/list')

        } catch (error) {
            console.error('requestBoardListToDjango(): ' + error)
            throw error
        }
    }
}