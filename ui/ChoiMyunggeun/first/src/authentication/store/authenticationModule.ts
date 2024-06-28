import actions, { AuthenticationActions } from "./actions"
import state, { AuthenticationState } from "./states"
import mutations, { AuthenticationMutations } from "./mutations"

export interface AuthenticationModule {
    namespaced: true
    state: AuthenticationState
    actions: AuthenticationActions
    mutations: AuthenticationMutations
}

const authenticationModule: AuthenticationModule = {
    namespaced: true,
    state,
    actions,
    mutations,
}

export default authenticationModule