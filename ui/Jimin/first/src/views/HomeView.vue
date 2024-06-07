<!-- 메인 홈페이지 부분 -->

<template>
  <hello-world />
</template>

<script lang="ts">
import { defineComponent } from 'vue';

// Components
import HelloWorld from '../components/HelloWorld.vue';

export default defineComponent({
  name: 'HomeView',

  components: {
    HelloWorld,
  },
});
</script>

