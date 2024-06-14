import { ActionContext } from "vuex"
import { AccountState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type AccountActions = {
    requestEmailDuplicationCheckToDjango(context: ActionContext<AccountState, any>, email: string): Promise<boolean>
    requestNicknameDuplicationCheckToDjango(context: ActionContext<AccountState, any>, payload: any): Promise<boolean>
}

const actions: AccountActions = {
    async requestEmailDuplicationCheckToDjango(context: ActionContext<AccountState, any>, email: string): Promise<boolean> {
        const response = await axiosInst.djangoAxiosInst.post(
            '/account/email-duplication-check', { email })
        return response.data.isDuplicate
    },

    async requestNicknameDuplicationCheckToDjango(context: ActionContext<AccountState, any>, payload: any): Promise<boolean> {
        const { newNickname } = payload
        return axiosInst.djangoAxiosInst.post(`/account/nickname-duplication-check`, { newNickname: newNickname })
            .then((res) => {
                if (res.data) {
                    alert('사용 가능한 닉네임입니다!')
                    return false
                } else {
                    alert('중복된 닉네임입니다!')
                    return true
                }
            })
    }
};

export default actions;