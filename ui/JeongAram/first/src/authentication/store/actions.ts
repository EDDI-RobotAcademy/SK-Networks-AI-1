import { ActionContext } from "vuex"
import { AuthenticationState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"


export type AuthenticationActions = {
    requestKaKaoOauthRedirectionToDjango(): Promise<void>
 
}

const actions: AuthenticationActions = {
    async requestKaKaoOauthRedirectionToDjango(): Promise<void> {
        return axiosInst.djangoAxiosInst.get('/oauth/kakao').then((res) => {
            console.log('requestKaKaoOauthRedirectionToDjango() -> res:', res.data.url)
            window.location.href = res.data.url
        }) 
    },  
};

export default actions;
