import { MutationTree } from "vuex";
import { AuthenticationState } from "./states";
import { REQUEST_IS_AUTHENTICATED_TO_DJANGO } from "./mutation-types";

export interface AuthenticationMutations extends MutationTree<AuthenticationState> {
    [REQUEST_IS_AUTHENTICATED_TO_DJANGO] (state: AuthenticationState, settingValue: boolean): void
}

const mutations: MutationTree<AuthenticationState> = {
    [REQUEST_IS_AUTHENTICATED_TO_DJANGO] (state: AuthenticationState, settingValue: boolean) {
        state.isAuthenticated = settingValue
    }
}

// 현재 Board Domain 만 다루고 있기 때문에 사실 아래와 같은 작업이 필요 없음
// 그러나 앞으로 추가할 것들을 고려한다면 예약어인 mutations를 피해야합니다.
// 고로 as를 사용하여 Board Domain 전용 Mutations라는 것을 표기하였습니다.
export default mutations as AuthenticationMutations