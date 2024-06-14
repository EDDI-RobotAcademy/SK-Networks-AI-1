import { ActionContext } from "vuex"
import { AuthenticationState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type AuthenticationActions = {
    requestKakaoOauthRedirectionToDjango(): Promise<void>
    // TypeScript에서 함수 작성 시 파라미터에는 아래와 같이 타입을 명시해야 합니다.
    // 파라미터 이름: 파라미터 타입 형태로 작성
    // 함수의 리턴 값은 파라미터를 표현하는 소괄호'(' 에서 시작해서 ')'로 끝난 지점 이후
    // ':' 을 사용하여 표현
    // 즉 testFunction(testNumber: number): number
    requestAccessTokenToDjangoRedirection(
        context: ActionContext<AuthenticationState, any>,
        payload: { code: string }): Promise<void>
    requestUserInfoToDjango(
        context: ActionContext<AuthenticationState, any>): Promise<any>
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

            return userInfo
        } catch (error) {
            alert('사용자 정보 가져오기 실패!');
            // JavaScript, TypeScript, python, TypeScript 등등
            // 최신 스펙을 가진 언어의 경우 세미콜론을 붙일 필요가 없습니다.
            // 보통 멀티 랭귀지 프로젝트에서는 Poly Glot(폴리 글랏)이란 것을 하게 됨
            // 세미콜론을 붙이는 습관이 있는 사람도 있고 없는 사람도 있기 때문에 혼선 방지 서포트 역할
            // 주로 MSA(Micro Service Architecture) 프로젝트를 하면 이런 상황이 비일비재
            throw error;
        }
    }
};

export default actions;