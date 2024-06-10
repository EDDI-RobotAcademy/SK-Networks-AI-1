import { ActionContext } from "vuex"
import { Board, BoardState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"
import { REQUEST_BOARD_LIST_TO_DJANGO } from "./mutation-types"

export type BoardActions = {
    requestBoardToDjango(context: ActionContext<BoardState, any>, boardId:number): Promise<void>
    requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void>
    requestCreateBoardToDjango(context: ActionContext<BoardState, unknown>, payload: {
        title: string, writer: string, content: string
    }): Promise<AxiosResponse>
}

const actions: BoardActions = {
    async requestBoardToDjango(context: ActionContext<BoardState, any>, boardId:number): Promise<void> {
        try {
            const res: AxiosResponse<Board> = await axiosInst.djangoAxiosInst.get(`/board/read/${boardId}`);
            console.log('data:', res.data)
            context.commit('REQUEST_BOARD_TO_DJANGO', res.data);
        } catch (error) {
            console.error('requestBoardToDjango()', error);
            throw error
        }
    },
    
    async requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void> {
        try {
            const res: AxiosResponse<any, any> = await axiosInst.djangoAxiosInst.get('/board/list/');
            console.log('data:', res)
            const data: Board[] = res.data;
            console.log('data:', data)
            context.commit('REQUEST_BOARD_LIST_TO_DJANGO', data);
        } catch (error) {
            console.error('Error fetching board list:', error);
            // 에러를 처리할 수 있는 추가 로직
            throw error
        }
    },
    async requestCreateBoardToDjango(context: ActionContext<BoardState, unknown>, payload: {
        title: string, writer: string, content: string
    }): Promise<AxiosResponse> {

        console.log('requestCreateBoardToDjango()')

        const { title, writer, content } = payload
        console.log('전송할 데이터:', { title, writer, content })

        try {
            // HTTP 통신을 진행할 때 유의할 사항이 있음
            // Get 방식과 POST 방식이 존재하는데
            // GET 방식은 URL에 모든 정보들이 노출됨
            // POST 방식은 URL에 정보가 노출되지 않고 데이터가 숨겨져서 보내짐
            // 고로 개인 정보나 민감한 데이터의 경우 반드시 POST로 전송할 필요가 있음
            // 보낼 때 첫 번째 인자가 '요청할 경로', 두 번째 인자는 데이터 형태로 보냅니다.
            const res: AxiosResponse = await axiosInst.djangoAxiosInst.post(
                '/board/register', { title, writer, content})

            console.log('res:', res.data)
            return res.data
        } catch (error) {
            alert('requestCreateBoardToDjango() 문제 발생!')
            throw error
        }
    }
};

export default actions;