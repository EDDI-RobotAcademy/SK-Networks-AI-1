import { ActionContext } from "vuex"
import { AuthenticationState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type AuthenticationActions = {
    requestKakaoOauthRedirectionToDjango(): Promise<void>
    // TypeScript에서 함수 작성 시
    // 파라미터에는 ㄹ아래와 같이 타입을 명시해야합니다.
    // 파라미터 이름: 파라미터 타입의 형태로 작성
    // 함수의 리턴 값은 파라미터를 표현하는
    // 소괄호 '(' 에서 시작해서 ')' 로 끝난 지점 이후
    // ':' 을 사용하여 표현

    // 즉 testFunction(testNumber: number): Promise<any>
    //
    requestAccessTokenToDjangoRedirection(
        context: ActionContext<AuthenticationState, any>, 
        payload: { code: string }): Promise<void>
    requestUserInfoToDjango(
        context: ActionContext<AuthenticationState, any>): Promise<any>
    requestAddRedisAccessTokenToDjango(
        context: ActionContext<AuthenticationState, any>,
        { email, accessToken }: { email: string, accessToken: string }): Promise<any>
}

const actions: AuthenticationActions = {
    async requestKakaoOauthRedirectionToDjango(): Promise<void> {
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
                await axiosInst.djangoAxiosInst.post(
                    '/oauth/kakao/user-info', 
                    { access_token: accessToken });
            
            console.log('User Info:', userInfoResponse.data.user_info);
            const userInfo = userInfoResponse.data.user_info
            console.log('userInfo:', userInfo)
            return userInfo
        } catch (error) {
            alert('사용자 정보 가져오기 실패!');
            // python, JavaScript, Golang, TypeScript 등등
            // 최신 스펙을 가진 언어의 경우
            // 세미콜론을 붙일 필요가 없습니다!
            // 보통 멀티 랭귀지 프로젝트에서는 Poly Glot이란 것을 하게 됨
            // 그래서 개발자들이 습관상 세미콜론을 붙이는 사람도 있고
            // 한동안 세미콜론을 붙이지 않던 사람들도 있어서
            // 그런 혼선을 방지하게 서포트하는 역할도 합니다.
            // 주로 MSA(Micro Service Architecture) 프로젝트를 하면 이런 상황이 비일비재함
            throw error;
        }
    },
    async requestAddRedisAccessTokenToDjango(
        context: ActionContext<AuthenticationState, any>,
        { email, accessToken }: { email: string, accessToken: string }): Promise<any> {
        try {
            console.log('requestAddRedisAccessTokenToDjango -> email:', email)
            console.log('requestAddRedisAccessTokenToDjango -> accessToken:', accessToken)
            const response: AxiosResponse<any> = await axiosInst.djangoAxiosInst.post(
                'oauth/redis-access-token', {
                    email: email,
                    accessToken: accessToken
                }
            )
            console.log('userToken:', response.data)
            localStorage.setItem('userToken', response.data)
            return response.data // Adjust according to what your API returns
        } catch (error) {
            console.error('Error adding redis access token:', error)
            throw error
        }
    }
};

export default actions;