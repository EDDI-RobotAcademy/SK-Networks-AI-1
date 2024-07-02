import { ActionContext } from "vuex"
import { AuthenticationState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"


export type AuthenticationActions = {
    requestKakaoOauthRedirectionToDjango(): Promise<void>
    // TypeScript에서 함수 작성 시
    
    // 파라미터에는 아래와 같이 타입을 명시해야합니다.
    // 파라미터 이름: 파라미터 타입 형태로 작성

    // 함수의 리턴 값은 파라미터를 표현하는
    // 소괄호'(' 에서 시작해서 ')'로 끝난 지점 이후
    // ':' 을 사용하여 표현

    // 즉 testFunction(testNumber: number): number
    // 위와 같은 형태로 표현된다는 뜻입니다.
    requestAccessTokenToDjangoRedirection(
        context: ActionContext<AuthenticationState, any>, 
        payload: { code: string }): Promise<void>
    requestUserInfoToDjango(
        context: ActionContext<AuthenticationState, any>): Promise<any>
    requestAddRedisAccessTokenToDjango(
        context: ActionContext<AuthenticationState, any>,
        { email, accessToken }: { email: string, accessToken: string }
    ): Promise<any>
    requestLogoutToDjango(
        context: ActionContext<AuthenticationState, any>,
        userToken: string
    ): Promise<void>
}

const actions: AuthenticationActions = {
    async requestKakaoOauthRedirectionToDjango(): Promise<void> {
        return axiosInst.djangoAxiosInst.get('/oauth/kakao').then((res) => {
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
            const userInfoResponse: AxiosResponse<any> = 
                await axiosInst.djangoAxiosInst.post(
                    '/oauth/kakao/user-info', 
                    { access_token: accessToken });

            const userInfo = userInfoResponse.data.user_info
            return userInfo

        } catch (error) {
            alert('사용자 정보 가져오기 실패!')
            throw error;
        }
    },
    async requestAddRedisAccessTokenToDjango(
        { commit, state }: ActionContext<AuthenticationState, any>,
        { email, accessToken }: { email: string, accessToken: string }
    ): Promise<any> {
        try {
            const response: AxiosResponse<any> = await axiosInst.djangoAxiosInst.post(
                '/oauth/redis-access-token/', {
                    email: email,
                    accessToken: accessToken
                });

            console.log('userToken:', response.data.userToken)

            localStorage.removeItem("accessToken")
            localStorage.setItem("userToken", response.data.userToken)
            commit('REQUEST_IS_AUTHENTICATED_TO_DJANGO', true);
            return response.data;
        } catch (error) {
            console.error('Error adding redis access token:', error);
            throw error;
        }
    },
    async requestLogoutToDjango(
        context: ActionContext<AuthenticationState, any>,
        userToken: string
    ): Promise<void> {

        try {
            const userToken = localStorage.getItem("userToken")

            const res = 
                await axiosInst.djangoAxiosInst.post('/oauth/logout', {
                    userToken: userToken
                })

            console.log('res:', res.data.isSuccess)
            if (res.data.isSuccess === true) {
                context.commit('REQUEST_IS_AUTHENTICATED_TO_DJANGO', false)
            }
        } catch (error) {
            console.error('requestPostToFastapi() 중 에러 발생:', error)
            throw error
        }
        localStorage.removeItem("userToken")
    }
};

export default actions;