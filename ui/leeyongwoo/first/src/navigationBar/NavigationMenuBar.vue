<template>
    <v-app-bar color="purple" app dark height="80">
        <v-btn @click="goToHome">
            <v-toolbar-title class="text-uppercase text--darken-4">
                <span style="font-family: Times New Roman, sans-serif; font-size: 20px; color: black;">SK Networks AI Camp with EDDI</span>
            </v-toolbar-title>
        </v-btn>
        <v-spacer></v-spacer>

        <!-- <v-menu>
            <template v-slot:activator="{ props }">
                <v-btn color="white" v-bind="props">
                    <b>Activator Slot</b>
                </v-btn>
            </template>
            <v-list>
                <v-list-item v-for="(item, index) in items" 
                            :key="index" :value="index" @click="item.action">
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu> -->

        <v-btn text @click="goToProductList" class="btn-text">
            <v-icon color="red" left>mdi-store</v-icon>
            <span style="font-family: Times New Roman, sans-serif; font-size: 20px; color: black;">Product</span>
        </v-btn>
        <v-btn color="black" text @click="goToBoardList" class="btn-text">
            <v-icon left>mdi-forum</v-icon>
            <span style="font-family: Times New Roman, sans-serif; font-size: 20px; color: black;">Board</span>
        </v-btn>
        <v-btn v-if="!isLogin" text @click="signIn" class="btn-text">
            <v-icon color="orange" left>mdi-login</v-icon>
            <span style="font-family: Times New Roman, sans-serif; font-size: 20px; color: black;">LogIN</span>
        </v-btn>
        <v-btn color="orange" v-if="isLogin" text @click="signOut" class="btn-text">
            <v-icon left>mdi-logout</v-icon>
            <span style="font-family: Times New Roman, sans-serif; font-size: 20px; color: black;">LogOut</span>
        </v-btn>
    </v-app-bar>

</template>

<script>
import '@mdi/font/css/materialdesignicons.css'
import router from '@/router'

export default {
    data () {
        return {
            navigation_drawer: false,
            // links: [{ icon: 'mdi-home', action: this.goToHome, route: '/' }],
            accessToken: null,
            isLogin: false,
            // items: [
            //     { title: 'Product', action: this.goToProductList() },
            //     { title: 'Board', action: this.goToBoardList() },
            // ]
        }
    },
    methods: {
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
            localStorage.removeItem("accessToken")
            this.isLogin = false
            router.push('/')
        },
        updateLoginStatus () {
            this.userToken = localStorage.getItem("userToken")
            this.isLogin = !!this.userToken
        }
    },
    mounted () {
        this.updateLoginStatus()
        window.addEventListener('storage', this.updateLoginStatus)
    },
    beforeUnmount () {
        window.removeEventListener('storage', this.updateLoginStatus)
    },
}
</script>
