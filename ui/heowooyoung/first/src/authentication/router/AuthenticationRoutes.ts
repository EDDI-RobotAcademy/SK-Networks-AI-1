import KakaoRedirection from "@/authentication/redirection/kakao/KakaoRedirection.vue"

const AuthenticationRoutes = [
    {
        path: '/oauth/kakao-access-token',
        name: 'KakaoRedirection',
        component: KakaoRedirection
    },
]

export default AuthenticationRoutes