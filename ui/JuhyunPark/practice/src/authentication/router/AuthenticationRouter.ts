import AccountLoginPage from "@/account/pages/AccountLoginPage.vue";
import KakaoRedirection from "../redirection/kakao/KakaoRedirection.vue";

const AuthenticationRoutes = [
    {
        path: '/oauth/kakao-access-token',
        name: 'KakaoRedirection',
        component: KakaoRedirection
    },
]