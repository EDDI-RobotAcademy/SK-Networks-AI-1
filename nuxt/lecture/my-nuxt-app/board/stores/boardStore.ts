import { defineStore } from "pinia"
import { boardState } from "./boardState"
import { boardActions } from "./boardActions"

export const useBoardStore = defineStore('boardStore', {
    state: boardState,
    actions: boardActions,
})