import { ActionContext } from "vuex"
import { ReportState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type ReportActions = {
    requestCreateReportToDjango(context: ActionContext<ReportState, unknown>, data: {
        age: number, genders: string}): Promise<AxiosResponse>
}

const actions: ReportActions = {
    async requestCreateReportToDjango(context: ActionContext<ReportState, unknown>, data: {
       age: number, genders: string}): Promise<AxiosResponse> {
        
        const userToken = localStorage.getItem('userToken')
        const { age, genders } = data

        const requestData = {
            data,
            userToken
        };
        console.log('requestData : ', requestData)


        try {
            const res: AxiosResponse = await axiosInst.djangoAxiosInst.post('/report/register', requestData )
            console.log('res:', res.data)
            return res.data
        } catch (error) {
            alert('requestCreateReportToDjango() 문제 발생!')
            throw error
        }
    }
};

export default actions;