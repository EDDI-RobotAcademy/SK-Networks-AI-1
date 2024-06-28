import actions, { PostActions } from "./actions";
import mutations, { PostMutations } from "./mutations";
import state, { PostState } from "./states";

export interface PostModule {
    namespaced: true;
    state: PostState;
    actions: PostActions;
    mutations: PostMutations;
}

const postModule: PostModule = {
    namespaced: true,
    state,
    actions,
    mutations,
};

export default postModule;
