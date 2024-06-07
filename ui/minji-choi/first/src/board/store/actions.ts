import {ActionContext} from 'vuex'
import {Board, BoardState} from './states'
import {AxiosResponse} from 'axios'
import axiosInst from "@/utility/axiosInstance"
import {REQUEST_BOARD_LIST_TO_DJANGO } from './mutation-types';
export type BoardActions = {
    requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void>

}

// async와 Promise는 비동기 통신을 사용하기 위해 반드시 필요합니다.
// 비동기 통신과 스레드, 병렬처리, 앞서 살펴봤던 process.env가 모두 연관되어 있습니다.
// 그래서 이 부분과 관련한 내용은 아마도 금요일 하루종일 설명해야 할 것 으로 판단됩니다. 매우 빡센이론
const actions: BoardActions = {
    async requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void> {
        try {
            const res: AxiosResponse<any,any> = await axiosInst.djangoAxiosInst.get('/board/list')
            const data: Board[] = res.data() 
            context.commit(REQUEST_BOARD_LIST_TO_DJANGO, data)
        } catch (error) {
            console.error('requestBoardListToDjango(): '+ error)
            throw error
        }
    }
}

export default actions
