<template>
  <v-app-bar color="orange" app dark height="64">
    <v-btn @click="goToHome">
      <v-toolbar-title class="text-uppercase text--darken-4">
        <span>SK Networks AI Camp with EDDI</span>
      </v-toolbar-title>
    </v-btn>
    <v-spacer></v-spacer>

    <v-menu close-on-content-click>
      <template #activator="{ props }">
        <v-btn color="black" v-bind="props">
          <b>Just for Test</b>
          <span v-if="isTestItemsProcessed()" class="status-indicator">!</span>
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in testItems"
          :key="index"
          @click="item.action"
        >
          <v-list-item-title>
            {{ item.title }}
            <span v-if="item.processed" class="status-indicator">!</span>
          </v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

    <v-menu close-on-content-click>
      <template #activator="{ props }">
        <v-btn color="black" v-bind="props">
          <b>Regression Analysis</b>
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
          @click="item.action"
        >
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
import { computed, onMounted, reactive } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const router = useRouter();
    // 이 부분 실제 board/stores 처럼 구성해서 사용해야 합니다(authentication/store)
    // const store = useStore();

    const state = reactive({
      items: [
        { title: 'Logistic Regression', action: () => router.push('/logistic-regression-result') },
        { title: 'Random Forest', action: () => router.push('/random-forest-result') },
        { title: 'Polynomial Regression', action: () => router.push('/polynomial-regression-result') },
        { title: 'Exponential Regression', action: () => router.push('/exponential-regression-result') },
      ],
      testItems: [
        { title: 'Kafka Test', processed: false, action: () => router.push('/kafka/test') },
        { title: 'Test Analysis 2', processed: false, action: () => router.push('/test-analysis-2-result') },
        { title: 'AI Request To Django', processed: false, action: () => router.push('/ai-request/send') },
      ],
      socket: null,
    });

    // 임시 방편으로 그냥 true 줬습니다
    const isAuthenticated = true
    // const isAuthenticated = computed(() => store.state.authenticationModule.isAuthenticated);

    const goToHome = () => {
      router.push('/');
    };

    const goToProductList = () => {
      router.push('/product/list');
    };

    const goToBoardList = () => {
      router.push('/board/list');
    };

    const goToPostPage = () => {
      router.push('/post/list');
    };

    const goToCart = () => {
      router.push('/cart/list');
    };

    const goToOrder = () => {
      router.push('/order/list');
    };

    const signIn = () => {
      router.push('/account/login');
    };

    const signOut = () => {
    //   store.dispatch('authenticationModule/requestLogoutToDjango');
      router.push('/');
    };

    const isTestItemsProcessed = () => {
      return state.testItems.some(item => item.processed);
    };

    const updateProcessingStatus = (data) => {
      if (data.message === "Processing completed.") {
        const item = state.testItems.find(item => item.title === data.title);
        if (item) {
          item.processed = true;
        }
      }
    };

    onMounted(() => {
      const userToken = localStorage.getItem("userToken");
      if (userToken) {
        // store.commit('authenticationModule/setAuthenticated', true);
      }

      // WebSocket connection logic
      // state.socket = new WebSocket('ws://192.168.0.18:33333/ws');
      // state.socket.onmessage = (event) => {
      //   const data = JSON.parse(event.data);
      //   updateProcessingStatus(data);
      // };
    });

    return {
      ...state,
      isAuthenticated,
      goToHome,
      goToProductList,
      goToBoardList,
      goToPostPage,
      goToCart,
      goToOrder,
      signIn,
      signOut,
      isTestItemsProcessed,
    };
  },
};
</script>

<style scoped>
.status-indicator {
  margin-left: 5px;
  font-weight: bold;
  color: red;
}
</style>
