import { MutationTree } from "vuex";
import { KafkaTestState, KafkaTestItem } from "./states";
import { REQUEST_KAFKA_TEST_DATA_TO_FASTAPI} from "./mutation-types";

export interface KafkaTestMutations extends MutationTree<KafkaTestState> {
    [REQUEST_KAFKA_TEST_DATA_TO_FASTAPI] (state: KafkaTestState, isRequest: boolean): void
}

const mutations: MutationTree<KafkaTestState> = {
    [REQUEST_KAFKA_TEST_DATA_TO_FASTAPI] (state: KafkaTestState, isRequest: boolean): void {
        state.isRequest = isRequest
    },
}

export default mutations as KafkaTestMutations