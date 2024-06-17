<template>
  <v-app>
    <!-- HTML 파트 -->
     <!-- 추가된 부분 -->
    <navigation-menu-bar/>  
    <!-- v-main 안에다 쓰면 vue를 키면 나오는 구성이 됨-->
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script lang="ts">
// Javascript 파트
import { defineComponent } from 'vue'
import NavigationMenuBar from './navigationBar/NavigationMenuBar.vue'

export default defineComponent({
  components: { NavigationMenuBar },
  name: 'App',

  data () {
    return {
      //
    }
  },
})
</script>

// 여기 하단에 CSS 파트