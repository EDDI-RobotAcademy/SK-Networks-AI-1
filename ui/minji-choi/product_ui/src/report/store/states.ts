export interface ReportState {
    reportList: ReportItem[]
}

export interface ReportItem {
    age: number
    gender: string
}

const state: ReportState = {
    reportList: [],
}

export default state