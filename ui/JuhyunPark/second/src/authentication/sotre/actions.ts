
import { ActionContext } from "vuex"
import { AuthenticationState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type AuthenticationActions = {
    requestKakaoOauthRedirectionToDjango(): Promise<void>
}

const actions: AuthenticationActions = {
    async requestKakaoOauthRedirectionToDjango(): Promise<void> {
        return axiosInst.djangoAxiosInst.get('/oauth/kakao').then((res) => {
            console.log('requestKakaoOauthRedirectionToDjango() -> res:', 
                        res.data.url)
            window.location.href = res.data.url
        })
    },
};

export default actions;
