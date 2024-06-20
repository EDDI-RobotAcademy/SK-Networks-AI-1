import KakaoRedirection from "@/authentication/redirection/kakao/KakaoRedirection.vue"
import router from "@/router"

const AuthenticationRoutes = [
    {
        path: '/oauth/kakao-access-token',
        name: 'KakaoRedirection',
        component: KakaoRedirection
    },
]

export default AuthenticationRoutes