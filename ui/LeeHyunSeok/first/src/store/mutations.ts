import { MutationTree } from "vuex";
import { BoardState,Board } from "./states";
import { REQUEST_BOARD_LIST_TO_DJANGO } from "./mutation-types";


export interface BoardMutations extends MutationTree<BoardState> {
    [REQUEST_BOARD_LIST_TO_DJANGO] (state: BoardState, receiveData: Board[]):void
}


const mutation: MutationTree<BoardState> = {
    [REQUEST_BOARD_LIST_TO_DJANGO] (state: BoardState, receiveData: Board[]): void{
        state.boards = receiveData
    }
}

export default