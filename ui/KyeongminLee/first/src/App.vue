<template>
  <v-app>
    <navigation-menu-bar/>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script lang="ts">
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
