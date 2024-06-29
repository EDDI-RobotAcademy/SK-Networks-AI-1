import { MutationTree } from "vuex";
import { KafkaTestState, KafkaTestItem } from "./states";
import {
    REQUEST_KAFKA_TEST_DATA_TO_FASTAPI
} from "./mutation-types";

export interface KafkaTestMutations extends MutationTree<KafkaTestState> {
    [REQUEST_KAFKA_TEST_DATA_TO_FASTAPI] (state: KafkaTestState, receivedData: KafkaTestItem): void
}

const mutations: MutationTree<KafkaTestState> = {
    [REQUEST_KAFKA_TEST_DATA_TO_FASTAPI] (state: KafkaTestState, receivedData: KafkaTestItem): void {
        state.kafkaTestData = receivedData
    },
}

export default mutations as KafkaTestMutations