import { ActionContext } from "vuex"
import { Board, BoardState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"
import { REQUEST_BOARD_LIST_TO_DJANGO } from "./mutation-types"
export type BoardActions = {requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void>}

const actions: BoardActions = {
async requestBoardListToDjango(context: ActionContext<BoardState, any>): Promise<void> {
    try {
    const res: AxiosResponse<any, any> = await axiosInst.djangoAxiosInst.get('/board/list/');
    const data: Board[] = res.data;
    context.commit('REQUEST_BOARD_LIST_TO_DJANGO', data);
    } catch (error) {
    console.error('Error fetching board list:', error);
    throw error
    }
}
};

export default actions;