import { ActionContext } from "vuex"
import { AccountState } from "./states"
import axios, { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type AccountActions = {
    requestEmailDuplicationCheckToDjango(
        context: ActionContext<AccountState, any>,
        email: string ): Promise<boolean>
}

const actions: AccountActions = {
    async requestEmailDuplicationCheckToDjango(
        context: ActionContext<AccountState, any>,
        email: string    ): Promise<boolean> {
            const response = await axiosInst.djangoAxiosInst.post('/account/email-duplication-check', { email })
  
        return response.data.isDuplicate //장고에서 맞추는 것/ axiosresponse는 dict형태로 온다??
        }
};

export default actions;