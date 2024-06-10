import { MutationTree } from "vuex";
import { BoardState, Board } from "./states";
import { REQUEST_BOARD_TO_DJANGO, REQUEST_BOARD_LIST_TO_DJANGO } from "./mutation-types";

export interface BoardMutations extends MutationTree<BoardState> {
    [REQUEST_BOARD_TO_DJANGO] (state: BoardState, receiveData: Board): void
    [REQUEST_BOARD_LIST_TO_DJANGO] (state: BoardState, receiveData: Board[]): void
}

const mutations: MutationTree<BoardState> = {
    [REQUEST_BOARD_TO_DJANGO] (state: BoardState, receiveData: Board): void {
        state.board = receiveData
    },
    [REQUEST_BOARD_LIST_TO_DJANGO] (state: BoardState, receiveData: Board[]): void {
        state.boards = receiveData
    }
}

export default mutations as BoardMutations