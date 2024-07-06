import actions, { ReportActions } from "./actions"
import state, { ReportState } from "./states"

export interface ReportModule {
    namespaced: true
    state: ReportState
    actions: ReportActions
}

const reportModule: ReportModule = {
    namespaced: true,
    state,
    actions,
}

export default reportModule