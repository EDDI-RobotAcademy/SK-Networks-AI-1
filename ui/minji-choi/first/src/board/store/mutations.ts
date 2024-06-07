import {MutationTree} from 'vuex'
import {BoardState, Board} from "./states"
import {REQUEST_BOARD_LIST_TO_DJANGO} from './mutation-types';

export interface BoardMutations extends MutationTree<BoardState> {
    [REQUEST_BOARD_LIST_TO_DJANGO] (state: BoardState, receiveData: Board[]): void
}

const mutations: MutationTree<BoardState> = {
    [REQUEST_BOARD_LIST_TO_DJANGO] (state: BoardState, receiveData: Board[]): void {
        state.boards = receiveData
    }
}

// 현재 Board Domain만 다루고 있기 때문에 아래와 같은 작업이 필요없긴 함
// 그러나 앞으로 추가할 것들을 고려한다면 예약어인 mutations를 피해야 합니다.
// 따라서 as 를 사용하여 Board Domain 전용 Mutations라는 것을 표기했습니다.
export default mutations as BoardMutations