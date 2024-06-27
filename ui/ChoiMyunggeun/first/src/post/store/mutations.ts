import { MutationTree } from "vuex";
import { PostState, Post } from "./states";
import { 
    REQUEST_POST_TO_FASTAPI,
    REQUEST_POST_LIST_TO_FASTAPI 
} from "./mutation-types";

export interface PostMutations extends MutationTree<PostState> {
    [REQUEST_POST_TO_FASTAPI] (state: PostState, receivedData: Post): void
    [REQUEST_POST_LIST_TO_FASTAPI] (state: PostState, receivedData: Post[]): void
}

const mutations: MutationTree<PostState> = {
    [REQUEST_POST_TO_FASTAPI] (state: PostState, receivedData: Post): void {
        state.post = receivedData
    },
    [REQUEST_POST_LIST_TO_FASTAPI] (state: PostState, receivedData: Post[]): void {
        state.postList = receivedData
    }
}

export default mutations as PostMutations