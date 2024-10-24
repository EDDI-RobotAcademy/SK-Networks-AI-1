import { defineStore } from "pinia"
import { aiRequestState } from "./aiRequestState"
import { aiRequestActions } from "./aiRequestActions"

export const useAiRequestStore = defineStore('aiRequestStore', {
    state: aiRequestState,
    actions: aiRequestActions,
})