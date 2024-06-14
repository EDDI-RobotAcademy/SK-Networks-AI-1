import { ActionContext } from "vuex"
import { AccountState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type AccountActions = {
    requestEmailDuplicationCheckToDjango(
        context: ActionContext<AccountState, any>,
        email: string
    ): Promise<boolean>
}

const actions: AccountActions = {
    async requestEmailDuplicationCheckToDjango(
        context: ActionContext<AccountState, any>,
        email: string
    ): Promise<boolean> {

        const response = await axiosInst.djangoAxiosInst.post(
            '/account/email-duplication-check', { email })
        return response.data.isDupliate
    },
};

export default actions;