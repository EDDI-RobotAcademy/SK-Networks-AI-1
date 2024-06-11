import { 
    REQUEST_BOARD_TO_DJANGO,
    REQUEST_BOARD_LIST_TO_DJANGO 
} from "./mutation-types";
import { BoardState, Board } from "./states";
import { MutationTree } from "vuex";

export interface BoardMutations extends MutationTree<BoardState> {
    [REQUEST_BOARD_LIST_TO_DJANGO](state: BoardState, receivedData: Board[]): void
    [REQUEST_BOARD_TO_DJANGO](state: BoardState, receivedData: Board): void
}

// interface의 Boards[]배열에 receiveData를 받는다
const mutations: MutationTree<BoardState>={
    [REQUEST_BOARD_LIST_TO_DJANGO](state: BoardState, receivedData: Board[]): void{
        state.boards = receivedData
    },
    [REQUEST_BOARD_TO_DJANGO](state: BoardState, receivedData: Board): void{
        state.board = receivedData
    }
}

// mutation이 예약어이기 때문에 이거 쓰면 다른 도메인에서 쓸 수 없기 때문에 변경
// Board Domain만 다룬다고 하면 바꿀 필요가 없음
export default mutations as BoardMutations