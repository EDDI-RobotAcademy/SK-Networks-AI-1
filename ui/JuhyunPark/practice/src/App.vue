<template>
  <v-app>
    <navigation-menu-bar/>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<!-- html 파트 -->

<script lang="ts">

// 자바스크립트 파트
import { defineComponent } from 'vue'
import NavigationMenuBar from './navigationBar/NaviationMenuBar.vue'

export default defineComponent({
  components: { NavigationMenuBar},
  name: 'App',

  data () {
    return {
      //
    }
  },
})
</script>
<!--  -->