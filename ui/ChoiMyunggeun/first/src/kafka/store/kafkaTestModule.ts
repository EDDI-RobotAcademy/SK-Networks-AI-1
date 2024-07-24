import mutations, { KafkaTestMutations } from "./mutations"
import state, { KafkaTestState } from "./states"
import actions, { KafkaTestActions } from "@/kafka/store/actions"

export interface KafkaTestModule{
    namespaced:true
    state:KafkaTestState
    actions:KafkaTestActions
    mutations:KafkaTestMutations
}
const kafkaTestModule: KafkaTestModule={
    namespaced:true,
    state,
    actions,
    mutations,
}

export default kafkaTestModule