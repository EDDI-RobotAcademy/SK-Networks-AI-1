import { ActionContext } from "vuex"
import { Board, BoardState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"
import { REQUEST_BOARD_LIST_TO_DJANGO, REQUEST_BOARD_TO_DJANGO } from "./mutation-types"

export type BoardActions = {
    requestBoardToDjango(context: ActionContext<BoardState, any>, boardId: number): Promise<void>
    requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void>
    requestCreateBoardToDjango(context: ActionContext<BoardState, unknown>, payload: {
        title: string, writer: string, content: string
    }): Promise<AxiosResponse>
    requestDeleteBoardToDjango(context: ActionContext<BoardState, unknown>, boardId: number): Promise<void>
    requestModifyBoardToDjango(context: ActionContext<BoardState, any>, payload:{
        title: string, content: string, boardId: number}): Promise<void>
}

const actions: BoardActions = {
    async requestBoardToDjango(context: ActionContext<BoardState, any>, boardId: number): Promise<void>{
        try {
            const res: AxiosResponse<Board> = await axiosInst.djangoAxiosInst.get(`/board/read/${boardId}`);
            console.log('data:',res.data)
            context.commit('REQUEST_BOARD_TO_DJANGO', res.data);
        } catch (error) {
            console.error('requestBoardToDjango() 문제 발생:', error);
            throw error
        }
    },
    async requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void> {
        try {
            const res: AxiosResponse<any, any> = await axiosInst.djangoAxiosInst.get('/board/list/');
            console.log('res:',res)
            const data: Board[] = res.data;
            console.log('data:', data)
            context.commit('REQUEST_BOARD_LIST_TO_DJANGO', data);
        } catch (error) {
            console.error('Error fetching board list:', error);
            // 에러를 처리할 수 있는 추가 로직
            throw error
        }
    },
    // 파라미터로 전달된 payload 외의 ActionContext라는 것이 존재함
    // 현재 vue에서 구동하는 action의 상태값을 관리하기 위해 사용
    // 이 context 객체를 사용하여 mutations를 호출할 수 있음
    // mutations를 호출하는 방식은 위의 list 케이스와 동일하게 context.commit()으로 호출함
    async requestCreateBoardToDjango(context: ActionContext<BoardState, unknown>, payload: {
        title: string, writer: string, content: string
    }): Promise<AxiosResponse> {

        console.log('requestCreateBoardToDjango()')

        const { title, writer, content } = payload
        console.log('전송할 데이터:', { title, writer, content })

        try {
            // HTTP 통신ㅇ르 진행할 때 유의할 사항이 있음
            // GET방식과 POST 방식이 존재하는데
            // GET 방식은 URL에 모든 정보들이 노출됨
            // POST 방식은 URL에  정보가 노출되지 않고, 
            const res: AxiosResponse = await axiosInst.djangoAxiosInst.post('/board/register', { title, writer, content})

            console.log('res:', res.data)
            return res.data
        } catch (error) {
            alert('requestCreateBoardToDjango() 문제 발생!')
            throw error
        }
    },
    async requestDeleteBoardToDjango(context: ActionContext<BoardState, unknown>, boardId: number): Promise<void>{
        try{
            console.log('requestDeleteBoardToDjango() ')
            // HTTP 상으로 DELETE 요청을 전송함
            await axiosInst.djangoAxiosInst.delete(`/board/delete/${boardId}`)
        } catch (error) {
            console.log('requestDeleteBoardToDjango() 과정에서 문제 발생!')
            throw error
        }
    },
    async requestModifyBoardToDjango(context: ActionContext<BoardState, any>, 
        payload:{ title: string, content: string, boardId: number}): Promise<void> {
        const { title, content, boardId} = payload
        try {
            await axiosInst.djangoAxiosInst.put(`/board/modify/${boardId}`, {title,content})
            console.log('수정 성공!')
        } catch (error) {
            console.log('requestModifyBoardToDjango() 과정에서 문제 발생')
            throw error
        }
    }
};

export default actions;