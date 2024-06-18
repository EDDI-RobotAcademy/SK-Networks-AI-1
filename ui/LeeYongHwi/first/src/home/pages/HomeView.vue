<template>
  <h1 class="orange-text" style="text-align: center; color: orange;">Home</h1>
  <v-row>
    <v-img class="mx auto"
         :src="require('@/assets/images/fixed/cs6.png')"
         height="300"/>
  </v-row>
  <v-row>
    <v-img class="mx auto"
         :src="require('@/assets/images/fixed/alone.png')"
         height="200"/>
  </v-row>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',

  components: {
  },
});
</script>

<style scoped>
.orange-text {
    margin-top: 40px;
}
</style>