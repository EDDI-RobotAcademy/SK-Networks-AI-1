import actions, { BoardActions } from "./actions"
import mutations, { BoardMutations } from "./mutations"
import state, { BoardState } from "./states"

export interface BoardModule {
    // namespaced가 true가 되면 앞서 *.vue 코드에서 봤듯이 아래와 같은 문법 허용
    // const boardModule = 'boardModule'
    // ...mapState(boardModule, ['boards'])
    // 즉 boardModule 자체를 위와 같이 참조할 수 있다는 의미
    namespaced: true
    state: BoardState
    actions: BoardActions
    mutations: BoardMutations
}

// python에서 싱글톤과 같은 역할
const boardModule: BoardModule = {
    namespaced: true,
    state,
    actions,
    mutations,
}

export default boardModule