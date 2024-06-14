<template>
    <v-container>
        <v-card>
            <v-img class="mx auto" height="300"
                    :src="require('@/assets/images/fixed/sk_ai_family.png')"/>        
        </v-card>
        <div class="login-icons">
            <v-img class="icon"
                    :src="require('@/assets/images/fixed/kakao_login.png')"
                    height="60"
                    @click="goToKaKaoLogin"/>
        </div>
    </v-container>
</template>

<script>
import { useStore } from 'vuex'

const authenticationModule = 'authenticationModule'

export default {
    setup () {
        const store = useStore()

        const goToKaKaoLogin = async () => {
            await store.dispatch("authenticationModule/requestKaKaoOauthRedirectionToDjango")
        }

        return { 
            goToKaKaoLogin
        }
    }

}
</script>

<style scoped>
.login_icons {
    margin-top: 20px   // 여백 추가
}

.icons {
    cursor: pointer;
}
</style>