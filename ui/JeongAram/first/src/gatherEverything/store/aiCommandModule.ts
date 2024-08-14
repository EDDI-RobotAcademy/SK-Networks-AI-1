import actions, { AICommandActions } from "./actions"
import mutations, { AICommandMutations } from "./mutations"
import state, { AICommandState } from "./states"

export interface AiCommandModule {
    namespaced: true
    state: AICommandState
    actions: AICommandActions
    mutations: AICommandMutations
}

const aiCommandModule: AiCommandModule = {
    namespaced: true,
    state,
    actions,
    mutations,
}

export default aiCommandModule