<template>
    <v-app-bar color="orange" app dark height="64">
        <v-btn @click="goToHome">
            <v-toolbar-title class="text-uppercase text--darken-4">
                <span>SK Networks AI Camp with EDDI</span>
            </v-toolbar-title>
        </v-btn>
        <v-spacer></v-spacer>

        <v-menu close-on-content-click>
            <template v-slot:activator="{ props }">
                <v-btn color="black" v-bind="props">
                    <b>Just for Test</b>
                    <span v-if="isTestItemsProcessed()" class="status-indicator">!</span>
                </v-btn>
            </template>
            <v-list>
                <v-list-item v-for="(item, index) in testItems" 
                            :key="index" @click="item.action">
                    <v-list-item-title>
                        {{ item.title }}
                        <span v-if="item.processed" class="status-indicator">!</span>
                    </v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>

        <v-menu close-on-content-click>
            <template v-slot:activator="{ props }">
                <v-btn color="black" v-bind="props">
                    <b>Regression Analysis</b>
                </v-btn>
            </template>
            <v-list>
                <v-list-item v-for="(item, index) in items"
                             :key="index" @click="item.action">
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
        <v-btn text @click="goToPostPage" class="btn-text">
            <v-icon left>mdi-forum</v-icon>
            <span>익명 게시판</span>
        </v-btn>
        <v-btn v-if="isAuthenticated" text @click="goToCart" class="btn-text">
            <v-icon left>mdi-cart</v-icon>
            <span>장바구니</span>
        </v-btn>
        <v-btn v-if="isAuthenticated" text @click="goToOrder" class="btn-text">
            <v-icon left>mdi-receipt</v-icon>
            <span>주문</span>
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
            // isLogin: !!localStorage.getItem("userToken"),
            items: [
                { title: 'Logistic Regression', action: () => { router.push('/logistic-regression-result') } },
                { title: 'Random Forest', action: () => { router.push('/random-forest-result') } },
                { title: 'Polynomial Regression', action: () => { router.push('/polynomial-regression-result') } },
                { title: 'Exponential Regression', action: () => { router.push('/exponential-regression-result') } }
            ],
            testItems: [
                { title: 'Kafka Test', processed: false, action: () => { router.push('/kafka/test') } },
                { title: 'Test Analysis 2', processed: false, action: () => { router.push('/test-analysis-2-result') } },
            ],
            socket: null
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
        goToCart () {
            router.push('/cart/list')
        },
        goToOrder () {
            router.push('/order/list')
        },
        goToPostPage () {
            router.push('/post/list')
        },
        updateProcessingStatus(data) {
            if (data.message === "Processing completed.") {
                console.log("처리 요청이 완료되었는지 체크")
                const item = this.testItems.find(item => item.title === data.title);
                if (item) {
                    item.processed = true;
                }

                // this.$store.state.kafkaTestModule.kafkaTestData = data
            }
        },
        isTestItemsProcessed() {
            return this.testItems.some(item => item.processed);
        }
    },
    mounted () {
        console.log('navigation bar mounted()')

        // this.socket = new WebSocket('ws://192.168.0.18:33333/ws');

        // this.socket.onmessage = (event) => {
        //     const data = JSON.parse(event.data);
        //     console.log('received data:', data)
        //     this.updateProcessingStatus(data);
        // };
        
        const userToken = localStorage.getItem("userToken")

        if (userToken) {
            console.log('You already have a userToken!!!')
            this.$store.state.authenticationModule.isAuthenticated = true
        }
    },
    beforeUnmount() {
        // WebSocket 연결 해제
        // this.socket.close();
    }
}
</script>


<style scoped>
.status-indicator {
    margin-left: 5px;
    font-weight: bold;
    color: red;
}
</style>