<template>
  <v-app>
    <navigation-menu-bar/>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script lang="ts">
// JavaScript 파트
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

// 여기 하단에 css 파트 (스타일 지정 가능)

