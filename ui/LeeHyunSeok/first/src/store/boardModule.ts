import { BoardState } from "./states"

export interface BoardModule{
    namespaced: true
    state: BoardState
    actions: BoardActions
    mutations: BoardMutations
}


const boardModule: BoardModule = {
    namespaced: true,
    state,
    actions,
    mutations,
}