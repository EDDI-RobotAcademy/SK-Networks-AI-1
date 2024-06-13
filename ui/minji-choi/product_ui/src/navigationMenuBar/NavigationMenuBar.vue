<template>
    <v-app-bar color="primary" app dark height="64">
        <v-btn @click="goToHome">
            <v-toolbar-title class="text-uppercase text--darken-4">
                <span>SK NETWORKS AI CAMP With MINN</span>
            </v-toolbar-title>
        </v-btn>
        <v-spacer></v-spacer>
        <v-menu>
            <template v-slot:actovator="{props}">
                <v-btn color="white" v-bind="props">
                    <b>Activator Slot 테스트</b>
                </v-btn>
        </template>
        <v-list>
            <v-list-item v-for="(item, index) in items" :key="index" :value="index" @click="item.action">
                <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
        </v-list>
        </v-menu>

        <v-btn text @click="goToProductList" class="btn-text">
            <v-icon left>mdi-store</v-icon>
            <span>상품</span>
        </v-btn>
        
    </v-app-bar>
</template>

<script>
import '@mdi/font/css/materialdesignicons.css'

export default {
    data () {
        return {
            navigation_drawer: false,
            links: [{icon: 'mdi-home', action: this.goToHome, route: '/'}],
            accessToken: null,
            isLogin: false,
            items: [
                {title: 'Product', action: this.goToProductList() },             
            ]
        }
    },
    methods: {
        goToHome () {
            console.log('홈입니다.')
        },
        goToProductList () {
            console.log('프로덕트 목록으로 리턴')
        }
    },
}
</script>