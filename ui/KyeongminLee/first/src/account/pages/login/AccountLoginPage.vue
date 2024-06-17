<template>
    <v-container>
        <v-row>
            <v-col v-for="n in 3" :key="n" class="d-flex child-flex" cols="4">
                <v-img class="mx auto" height="200"
                        :src="require('@/assets/images/fixed/caat.jpg')"
                        aspect-ration="1"
                        cover />
            </v-col>
        </v-row>
        <div class="login_icons">
            <v-img class="icons" 
                    :src="require('@/assets/images/fixed/kakao_login_medium_narrow.png')"
                    height="100"
                    @click="goToKaKoLogin"/>
        </div>
    </v-container>
</template>

<script>
import { useStore } from 'vuex'

const authenticationModule = 'authenticationModule'

export default {
    setup() {
        const store = useStore()

        const goToKaKoLogin = async () => {
            // ...mapActions이랑 동일한 방식
            await store.dispatch("authenticationModule/requestKakaoOauthRedirectionToDjango")
        }

        return {
            goToKaKoLogin
        }
    }
}
</script>


<style scoped>
.login_icons {
    margin-top: 80px;
}
.icons {
    cursor: pointer;
}

</style>