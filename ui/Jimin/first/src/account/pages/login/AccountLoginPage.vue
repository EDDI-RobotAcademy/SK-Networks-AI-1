<template>
    <v-container>
        
        <v-img class="mx auto" height="300" :src="require('@/assets/images/fixed/sk_family_ai.png')"/>
        
        <div class="login-icons">
            <v-img class="icon" :src="require('@/assets/images/fixed/loglog.jpg')" height="300" @click="goToKakaoLogin"/>
        </div>
    </v-container>
</template>

<script>
import { useStore } from 'vuex';

const authenticationModule = 'authenticationModule'

export default{
    setup() {
        const store = useStore()

        const goToKakaoLogin = async () => {
            await store.dispatch("authenticationModule/requestKakaoOauthRedirectionToDjango")
        }

        return {
            goToKakaoLogin
        }
    }

}
</script>

<style scoped>
.login_icons {
    margin-top: 20px;
}

.icons {
    cursor: pointer;
}
</style>