import { ActionContext } from "vuex"
import { AuthenticationState } from "./states"
import axios, { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type AuthenticationActions = {
    requestKakaoOauthRedirectionToDjango(): Promise<void>
    requestAccessTokenToDjangoRedirection(context: ActionContext<AuthenticationState, any>, 
                                          payload: { code: string }): Promise<void>
    requestUserInfoToDjango(context: ActionContext<AuthenticationState, any>): Promise<any>}


const actions: AuthenticationActions = {
    async requestKakaoOauthRedirectionToDjango(): Promise<void> {
        // TS 에서 함수 작성시 파라미터에는 아래와 같이 타입을 명시해야함. 
        // 파라미터 이름: ㅍ라미터 타입 -> 이 형태로 작성
        // 함수의 리턴값을 파라미터를 표현하는 '('에서 시작해서 ')'로 끝난 지점이후 ':'를 사용하여 표현
        // 즉, testFunc (testnumber : number)
        // 위와 같이표시된다는 말 
        return axiosInst.djangoAxiosInst.get('/oauth/kakao').then((res) => {
            console.log('requestKakaoOauthRedirectionToDjango() -> res:', 
                        res.data.url)
            window.location.href = res.data.url
        })
    },
    async requestAccessTokenToDjangoRedirection(
                context: ActionContext<AuthenticationState, any>, 
                payload: { code: string }): Promise<void> {
        try {
            console.log('requestAccessTokenToDjangoRedirection()')
            const { code } = payload

            const response = await axiosInst.djangoAxiosInst.post(
                '/oauth/kakao/access-token', { code })
            console.log('accessToken:', response.data.accessToken.access_token)
            localStorage.setItem("accessToken", response.data.accessToken.access_token)
        } catch (error) {
            console.log('Access Token 요청 중 문제 발생:', error)
            throw error
        }
    },
    async requestUserInfoToDjango(
            context: ActionContext<AuthenticationState, any>): Promise<any> {

        try {
            const accessToken = localStorage.getItem("accessToken");
            console.log('accessToken:', accessToken);
            const userInfoResponse: AxiosResponse<any> = 
                await axiosInst.djangoAxiosInst.post('/oauth/kakao/user-info', { access_token: accessToken });
            
            console.log('User Info:', userInfoResponse.data.user_info);
            const userInfo = userInfoResponse.data.user_info
            // const email = userInfoResponse.data.user_info.kakao_account.email
            // console.log('email :', email)
            return userInfo;
            
        } catch (error) {
            alert('사용자 정보 가져오기 실패!');
            throw error;
        }
    }
};

export default actions;