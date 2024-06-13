<template>
    <v-app-bar color="primary" app dark height="64">
        <v-btn @click="goToHome">
            <v-toolbar-title class="text-uppercase text--darken-4">
                <span>SK Networks AI Camp with EDDI</span>
            </v-toolbar-title>
        </v-btn>
        <v-spacer></v-spacer>

        <v-menu>
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
        </v-menu>

        <v-btn text @click="goToProductList" class="btn-text">
            <v-icon left>mdi-store</v-icon>
            <span>상품</span>
        </v-btn>
        <v-btn text @click="goToBoardList" class="btn-text">
            <v-icon left>mdi-forum</v-icon>
            <span>게시판</span>
        </v-btn>
    </v-app-bar>
</template>

<script>
import '@mdi/font/css/materialdesignicons.css'

export default {
    data () {
        return {
            navigation_drawer: false,
            links: [{ icon: 'mdi-home', action: this.goToHome, route: '/' }],
            accessToken: null,
            isLogin: false,
            items: [
                { title: 'Product', action: this.goToProductList() },
                { title: 'Board', action: this.goToBoardList() },
            ]
        }
    },
    methods: {
        goToHome () {
            console.log('호미다')
        },
        goToProductList () {
            console.log('프로덕트')
        },
        goToBoardList () {
            console.log('보드')
        },
    }
}
</script>
