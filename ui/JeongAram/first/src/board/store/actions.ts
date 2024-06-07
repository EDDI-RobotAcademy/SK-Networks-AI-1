import { ActionContext } from "vuex"
import { BoardState } from "./states"
import { REQUEST_BOARD_LIST_TO_DJANGO } from "./mutation-types"
import axiosInst from "@/utility/axiosInstance"
import { AxiosResponse } from "axios"

export type BoardActions = {
    requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void>
}

// async 와 Promise는 비동기 통신을 사용하기 위해 반드시 필요합니다.
// 비동기 통신과 스레드, 병렬 처리, 앞서 살펴봤던 process.env가 모두 연관되어 있습니다.
// 그래서 이 부분과 관련한 내용은 아마도 금요일 하루 종일 설명 예정
// 이론이 매우 빡센 부분

// 이 부분을 간략하게 정리해보고자 한다면 아래 내용 참고
// https://www.notion.so/eddi-robot-academy/thread-89c983d487ea4008998f1faeef6e2401
const actions: BoardActions = {
    async requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void>{
        try {
            const res: AxiosResponse<any, any> =
                await axiosInst.djangoAxiosInst.get('/board/list')

            const data: Board[] = res.data
            context.commit(REQUEST_BOARD_LIST_TO_DJANGO, data)    
        }catch (error){
            console.error('requestBoardListTodjango(): ' + error)
            throw error
        }
    }
}

export default actions