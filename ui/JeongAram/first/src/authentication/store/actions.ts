import { ActionContext } from "vuex"
import { AuthenticationState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"


export type AuthenticationActions = {
    requestKaKaoOauthRedirectionToDjango(): Promise<void>
    requestAccessTokenToDjangoRedirection(
        context: ActionContext<AuthenticationState, any>,
        payload: { code: string }): Promise<void>
    
 
}

const actions: AuthenticationActions = {
    async requestKaKaoOauthRedirectionToDjango(): Promise<void> {
        return axiosInst.djangoAxiosInst.get('/oauth/kakao').then((res) => {
            console.log('requestKaKaoOauthRedirectionToDjango() -> res:', res.data.url)
            window.location.href = res.data.url
        }) 
    },
    async requestAccessTokenToDjangoRedirection(
        context: ActionContext<AuthenticationState, any>,
        payload: { code: string }): Promise<void> {
    
    try {
        console.log('requestAccessToDjangoRedirection()')
    const { code } = payload

    const response = axiosInst.djangoAxiosInst.post(
        '/oauth/kakao/access-token', { code })
    console.log('accessToken:', (await response).data.accessToken.access_token)
    } catch (error) {
        console.log('Access Token 요청 중 문제 발생:', error)
        throw error
    }

    
    }
     
};

export default actions;
