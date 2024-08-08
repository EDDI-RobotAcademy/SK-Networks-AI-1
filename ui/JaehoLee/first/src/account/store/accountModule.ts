import actions, { AccountActions } from "./actions"
import state, { AccountState } from "./states"


export interface AccountModule {
    namespaced: true
    state: AccountState
    actions: AccountActions
    // mutations: AuthenticationMutations
}

const accountModule: AccountModule = {
    namespaced: true,
    state,
    actions,
    // mutations,
}

export default accountModule