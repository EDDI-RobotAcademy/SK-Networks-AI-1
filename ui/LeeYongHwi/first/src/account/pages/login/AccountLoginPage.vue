<template>
    <v-container>
        <v-card>
            <v-row>
                <v-col v-for="image in images" :key="image" class="d-flex child-flex" cols="4">
                    <v-img class="mx auto" height="300"
                            :src="require(`@/assets/images/fixed/${image}`)"
                            aspect-ration="1"
                            />
                    </v-col>
            </v-row>
        </v-card>
        <div class="login-icons">
            <v-img class="icons"
                   :src="require('@/assets/images/fixed/kakao_login.png')"
                   height="100"
                   @click="goToKakaoLogin"/>
        </div>
    </v-container>
</template>

<script>
import { useStore } from 'vuex'

const authenticationModule = 'authenticationModule'

export default {
    data () {
        return {
            images: ['cs1.png', 'cs2.png', 'cs3.png']
        }
    },
    setup () {
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
.login-icons {
    margin-top: 30px;
}

.icons {
    cursor: pointer;
}
</style>