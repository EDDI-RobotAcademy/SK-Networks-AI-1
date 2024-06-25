<template>
    <v-app-bar color="orange" app dark height="64">
        <v-btn @click="goToHome">
            <v-toolbar-title class="text-uppercase text--darken-4">
                <span>SK Networks AI Camp with EDDI</span>
            </v-toolbar-title>
        </v-btn>
        <v-spacer></v-spacer>

        <v-btn text @click="goToProductList" class="btn-text">
            <v-icon left>mdi-store</v-icon>
            <span>상품</span>
        </v-btn>
        <v-btn text @click="goToBoardList" class="btn-text">
            <v-icon left>mdi-forum</v-icon>
            <span>게시판</span>
        </v-btn>
        <v-btn v-if="!isAuthenticated" text @click="signIn" class="btn-text">
            <v-icon left>mdi-login</v-icon>
            <span>로그인</span>
        </v-btn>
        <v-btn v-if="isAuthenticated" text @click="signOut" class="btn-text">
            <v-icon left>mdi-logout</v-icon>
            <span>로그아웃</span>
        </v-btn>
    </v-app-bar>
</template>

<script>
import '@mdi/font/css/materialdesignicons.css'
import router from '@/router'
import { mapActions, mapState } from 'vuex'

const authenticationModule = 'authenticationModule'

export default {
    data () {
        return {
            isLogin: !!localStorage.getItem("userToken")
        }
    },
    computed: {
        ...mapState(authenticationModule, ['isAuthenticated'])
    },
    methods: {
        ...mapActions(authenticationModule, ['requestLogoutToDjango']),
        goToHome () {
            router.push('/')
        },
        goToProductList () {
            router.push('/product/list')
        },
        goToBoardList () {
            router.push('/board/list')
        },
        signIn () {
            router.push('/account/login')
        },
        signOut () {
            this.requestLogoutToDjango()
            router.push('/')
        },
    },
    mounted () {
        window.addEventListener('storage', this.updateLoginStatus)
    },
    beforeUnmount () {
        window.removeEventListener('storage', this.updateLoginStatus)
    },
}
</script>
