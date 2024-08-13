import { MutationTree } from "vuex";
import { AICommandState } from "./states";
import { 
    REQUEST_AI_COMMAND_RESULT_TO_FASTAPI 
} from "./mutation-types";

export interface AICommandMutations extends MutationTree<AICommandState> {
    [REQUEST_AI_COMMAND_RESULT_TO_FASTAPI] (state: AICommandState, receivedData: any): void
}

const mutations: MutationTree<AICommandState> = {
    [REQUEST_AI_COMMAND_RESULT_TO_FASTAPI] (state: AICommandState, receivedData: any): void {
        state.aiCommandResult = receivedData
    }
}

export default mutations as AICommandMutations