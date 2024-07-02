<template>
    <v-app-bar color="primary" app dark height="64">
        <v-btn @click="goToHome">
            <v-toolbar-title class="text-uppercase text--darken-4">
                <span>SK Networks AI Camp with EDDI</span>
            </v-toolbar-title>
        </v-btn>
        <v-spacer></v-spacer>

        <!-- <v-menu> -->
            <!-- <template v-slot:activator="{ props }">
                <v-btn color="white" v-bind="props">
                    <b>Activator Slot 테스트</b>
                </v-btn>
            </template>
            <v-list>
                <v-list-item v-for="(item, index) in items" :key="index" :value="index" @click="item.action">
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
            </v-list> -->
        <!-- </v-menu> -->

        <v-btn text @click="goToProductList" class="btn-text">
            <v-icon left>mdi-store</v-icon>
            <span>상품</span>
        </v-btn>
        <v-btn text @click="goToBoardList" class="btn-text">
            <v-icon left>mdi-store</v-icon>
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
import router from'@/router'
import { mapState, mapActions } from 'vuex'

const authenticationModule = 'authenticationModule'


export default{
    data () {
        return {
            navigation_drawer: false,
            // links: [{icon: 'mdi-home', action: this.goToHome, route: '/'}],
            accessToken: null,
            isLogin: false,
            // items: [
            //     {title: 'Porduct', action: this.goToProductList() },
            //     {title: 'Board', action: this.goToBoardList() }

            // ]
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
        updateLoginStatus () {
            this.userToken = localStorage.getItem("userToken")
            this.isLogin = !!this.userToken
        }
    },
    mounted () {
        // this.updateLoginStatus()
        // window.addEventListener('storage', this.updateLoginStatus)
        const userToken = localStorage.getItem("userToken")

        if(userToken !== '') {
            console.log('You already has a userToken!!')
            // this.$store를 통해 Vue가 관리하는 Vuex 스토리지 접근
            // Vuex 내에 존재하는 state 중 우리가 모듈로 만든
            // authenticationModule의 isAuthenticated에 접근
            // 실제 위의 ...mapState로 간편하게 접근했지만
            // mount 중에서는 불가하므로 아래와 같이 직접 처리
            this.$store.state.authenticationModule.isAuthenticated = true
        }
        
    },
    // beforeUnmount () {
    //     window.removeEventListener('storage', this.updateLoginStatus)
    // }
}
</script>