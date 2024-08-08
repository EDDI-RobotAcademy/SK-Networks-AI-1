<template>
    <v-container>
        <v-card flat>
            <v-img class="mx auto" height="300" :src="require('@/assets/images/fixed/login_img.png')"/>
        </v-card>
        <div class="login-icons">
            <v-img class="icon" 
                    :src="require('@/assets/images/fixed/login_button.webp')" 
                    height="60" @click="goToKaKaoLogin"/>
        </div>
    </v-container>
</template>

<script>
import { useStore} from 'vuex'

const authenticationModule = 'authenticationModule'

export default {
    setup () {
        const store = useStore()

        const goToKaKaoLogin = async () => {
            await store.dispatch("authenticationModule/requestKakaoOauthRedirectionToDjango")
        }
    return {
        goToKaKaoLogin
    }
}

}</script>

<style scoped>
    .login_icons {
        margin-top: 20px;
    }
    .icons {
        cursor: pointer;
    }

</style>