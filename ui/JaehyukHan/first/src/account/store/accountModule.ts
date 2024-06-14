import actions, { AccountActions } from "./actions"
import state, { AccountState } from "./states"

export interface AccountModule {
    namespaced: true
    state: AccountState
    actions: AccountActions
    // mutation:
}

const accountModule: AccountModule = {
    namespaced: true,
    state,
    actions,
    // mutation,
}

export default accountModule