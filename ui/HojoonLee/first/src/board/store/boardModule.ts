import actions, { BoardActions } from "./actions"
import mutations, { BoardMutations } from "./mutations"
import state, { Board, BoardState } from "./states"

export interface BoardModule {
    // namespace가 true이면 앞서 *.vue 코드에서 살펴봤듯이
    // 아래와 같은 문법이 허용됩니다
    // const boardModule = 'boardModule'
    // ...mapState(boardModule, ['boards'])
    // 즉 namespace 덕분에 boardModule 자체를 위와 같이 참조할 수 있다는 의미입니다.
    namespaced : true
    state : BoardState
    actions : BoardActions
    mutations : BoardMutations
}

const boardModule: BoardModule = {
    namespaced: true,
    state, // state를 통해 객체가 있다면 굳이 더 하지 않음 (싱글톤의 기능)
    actions,
    mutations,
}

export default boardModule