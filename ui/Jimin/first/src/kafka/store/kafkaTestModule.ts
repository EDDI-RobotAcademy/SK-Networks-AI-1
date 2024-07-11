import actions, { KafkaTestActions } from "./actions"
import mutations, { KafkaTestMutations } from "./mutations"
import state, { KafkaTestState } from "./states"

export interface KafkaTestModule {
    namespaced: true
    state: KafkaTestState
    actions: KafkaTestActions
    mutations: KafkaTestMutations
}

const kafkaTestModule: KafkaTestModule = {
    namespaced: true,
    state,
    actions,
    mutations
}

export default kafkaTestModule