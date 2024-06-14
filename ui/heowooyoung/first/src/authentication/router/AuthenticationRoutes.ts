import KaKaoRedirection from "@/authentication/redirection/kakao/KaKaoRedirection.vue";

const AuthenticationRoutes = [
    {
        path: '/oauth/kakao-access-token',
        name: 'kakaoRedirection',
        component: KaKaoRedirection
    },
]

export default AuthenticationRoutes