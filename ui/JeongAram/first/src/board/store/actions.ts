import { ActionContext } from "vuex"
import { Board, BoardState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"
import { REQUEST_BOARD_LIST_TO_DJANGO } from "./mutation-types"

export type BoardActions = {
    requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void>
    requestCreateBoardToDjango(context: ActionContext<BoardState, unknown>, payload: {
        title: string, writer: string, content: string
    }): Promise<AxiosResponse>
}

// async와 Promise는 비동기 통신을 사용하기 위해 반드시 필요합니다.
// 비동기 통신과 스레드, 병렬 처리, 앞서 살펴봤던 process.env가 모두 연관되어 있습니다.
// 그래서 이 부분과 관련한 내용은 아마도 금요일 하루 종일 설명해야 할 것으로 판단됩니다.
// 이론이 매우 빡센 부분입니다.

// 이 부분을 간략하게 정리해보고자 한다면 아래 내용을 읽어보면 좀 더 도움이 될 것 같습니다.
// https://www.notion.so/eddi-robot-academy/thread-89c983d487ea4008998f1faeef6e2401
const actions: BoardActions = {
    async requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void> {
        try {
            const res: AxiosResponse<any, any> = 
                await axiosInst.djangoAxiosInst.get('/board/list')
            
            const data: Board[] = res.data
            context.commit(REQUEST_BOARD_LIST_TO_DJANGO, data)
        } catch (error) {
            console.error('requestBoardListToDjango(): ' + error)
            // 에러를 처리할 수 있는 추가 로직
            throw error
        }
    },
    // async, Promise는 추후에 논의
    // 파라미터로 전달된 payload 외의 ActionContext 라는 것이 존재함
    // 현재 vue에서 구동하는 action의 상태값을 관리하기 위해 사용
    // 이 context 객체를 사용하여 mutation를 호출 할 수 있음
    // mutations을 호출하는 방식은 위의 list 케이스와 동일하게 context.commit()으로 호출함
    async requestCreateBoardToDjango(context: ActionContext<BoardState, unknown>, payload: {
        title: string, writer: string, content: string
    }): Promise<AxiosResponse> {

        console.log('requestCreateBoardToDjango()')

        const{ title, writer, content } = payload
        console.log('전송할 데이터:', {title, writer, content })

        try {
            //HTTP 통신을 진행할 때 유의할 사항이 있음
            // GET 방식와 POST 방식이 존재하는데
            // GET 방식은 URL에 모든 정보들이 노출됨
            // POST 방식은 URL에 정보가 노출되지 않고 데이터가 숨겨져서 보내짐
            // 고로 개인 정보나 민감한 데이터의 경우 반드시 POST로 전송할 필요가 있음
            // 보낼 때 첫 번째 인자가 '요청할 경로', 두 번째 인자는 데이터 형태로 보냅니다.
            const res: AxiosResponse = await axiosInst.djangoAxiosInst.post(
                '/board/register', { title, writer, content})
            
                console.log('res', res.data)
                return res.data
        } catch(error) {
            alert('requestCreateBoardToDjango() 문제 발생!')
            throw error
        }
    }
}

export default actions;