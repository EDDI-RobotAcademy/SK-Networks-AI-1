import { MutationTree } from "vuex";
import { BoardState, Board } from "./states";
import { REQUEST_BOARD_LIST_TO_DJANGO } from "./mutation-types";

export interface BoardMutations extends MutationTree<BoardState>{
    [REQUEST_BOARD_LIST_TO_DJANGO] (state: BoardState, receiveData: Board[]): void
}

// resquest to django했을때 받아오는 데이터 (receivedata)를 배열에 담아옴
const mutations: MutationTree<BoardState> = {
    [REQUEST_BOARD_LIST_TO_DJANGO] (state: BoardState, receiveData: Board[]): void{
        state.boards = receiveData
    }
}

// mutations를 BoardMutations라 다시 이름을 명명한이유
// mutations는 예약어라 여러 도메인에 쓰일 시 분간이 안 되기 때문에
// Board에서만 쓰일 예약어라고 명명
export default mutations as BoardMutations