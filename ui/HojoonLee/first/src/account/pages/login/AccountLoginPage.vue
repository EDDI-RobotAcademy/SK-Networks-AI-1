<template>
    <v-container>
        <v-card>
            <v-img class="mx auto" height="300" 
                :src="require('@/assets/images/fixed/sk_ai_family.png')"/>
        </v-card>
            <v-img class="icon"
                    :src="require('@/assets/images/fixed/kakao_login.png')"
                    height="60"
                    @click="goToKakaoLogin"/>
    </v-container>
</template>

<script>
import authenticationModule from '@/authentication/store/authenticationModule';
import {useStore} from 'vuex'

export default {
    setup () {
        const store = useStore()

        const goToKakaoLogin = async () => {
            await store.dispatch("authenticationModule/requestKakaoOauthRedirectionToDjango")
        }

        return {
            goToKakaoLogin
        }
    }
}</script>

<style scoped>
.login_icons {
    margin-top: 20px;
}
.icons{
    cursor: pointer;
}
</style>