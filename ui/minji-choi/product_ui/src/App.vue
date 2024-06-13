<template>
  <v-app>
    <!-- HTML 파트 -->
    <navigation-menu-bar/>  <!-- 항상 모든 페이지 위에 있도록 -->
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script lang="ts">
// 자바스크립트 파트
import NavigationMenuBar from './navigationMenuBar/NavigationMenuBar.vue'
import { defineComponent } from 'vue'

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
<!-- 여기 하단에 CSS 작업(style 지정) 파트 -->
