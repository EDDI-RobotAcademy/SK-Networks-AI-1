<template>
  <v-app id="inspire">
    <v-app-bar color="green" app dark height="64">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-app-bar-title>Application</v-app-bar-title>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" temporary>
      <!--  -->
    </v-navigation-drawer>

    <v-main class="bg-yellow-lighten-5">
      <v-container>

        <!-- 카테고리 1 -->
        <v-row>
          <v-col class="mt-2" cols="12">
            <strong>#인기있는</strong>
          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-1-1"></v-sheet>
            <h2 style="font-size: 16px;">인기 있는 춘식1</h2>
          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-1-2"></v-sheet>
            <h2 style="font-size: 16px;">인기 있는 춘식2</h2>
          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-1-3"></v-sheet>
            <h2 style="font-size: 16px;">인기 있는 춘식3</h2>
          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-1-4"></v-sheet>
            <h2 style="font-size: 16px;">인기 있는 춘식4</h2>
          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-1-5"></v-sheet>
            <h2 style="font-size: 16px;">인기 있는 춘식5</h2>
          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-1-6"></v-sheet>
            <h2 style="font-size: 16px;">인기 있는 춘식6</h2>
          </v-col>
        </v-row>

        <!-- 카테고리 2 -->
        <v-row>
          <v-col class="mt-2" cols="12">
            <strong>#귀여운</strong>
          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-2-1"></v-sheet>
            <h2 style="font-size: 16px;">귀여운 춘식1</h2>

          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-2-2"></v-sheet>
            <h2 style="font-size: 16px;">귀여운 춘식2</h2>

          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-2-3"></v-sheet>
            <h2 style="font-size: 16px;">귀여운 춘식3</h2>

          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-2-4"></v-sheet>
            <h2 style="font-size: 16px;">귀여운 춘식4</h2>

          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-2-5"></v-sheet>
            <h2 style="font-size: 16px;">귀여운 춘식5</h2>

          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-2-6"></v-sheet>
            <h2 style="font-size: 16px;">귀여운 춘식6</h2>

          </v-col>
        </v-row>

        <!-- 카테고리 3 -->
        <v-row>
          <v-col class="mt-2" cols="12">
            <strong>#재미있는</strong>
          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-3-1"></v-sheet>
            <h2 style="font-size: 16px;">재미있는 춘식1</h2>

          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-3-2"></v-sheet>
            <h2 style="font-size: 16px;">재미있는 춘식2</h2>

          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-3-3"></v-sheet>
            <h2 style="font-size: 16px;">재미있는 춘식3</h2>

          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-3-4"></v-sheet>
            <h2 style="font-size: 16px;">재미있는 춘식4</h2>

          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-3-5"></v-sheet>
            <h2 style="font-size: 16px;">재미있는 춘식5</h2>

          </v-col>
          <v-col cols="6" md="2">
            <v-sheet height="150" class="image-sheet image-3-6"></v-sheet>
            <h2 style="font-size: 16px;">재미있는 춘식6</h2>

          </v-col>
        </v-row>

      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from 'vue'

const drawer = ref(null)
const categories = ['#인기있는', '#귀여운', '#재미있는']
</script>

<script>
export default {
  data: () => ({ drawer: null }),
}
</script>

<style>
.image-sheet {
  background-size: cover;
  /* 이미지를 네모에 꽉 채우기 */
  background-position: center;
  /* 이미지를 중앙에 배치 */
  background-repeat: no-repeat;
  /* 이미지를 반복하지 않기 */
}

.image-1-1 {
  background-image: url('@/assets/images/fixed/1.png');
}

.image-1-2 {
  background-image: url('@/assets/images/fixed/2.png');
}

.image-1-3 {
  background-image: url('@/assets/images/fixed/3.png');
}

.image-1-4 {
  background-image: url('@/assets/images/fixed/4.png');
}

.image-1-5 {
  background-image: url('@/assets/images/fixed/5.png');
}

.image-1-6 {
  background-image: url('@/assets/images/fixed/6.png');
}

.image-2-1 {
  background-image: url('@/assets/images/fixed/7.png');
}

.image-2-2 {
  background-image: url('@/assets/images/fixed/8.png');
}

.image-2-3 {
  background-image: url('@/assets/images/fixed/9.png');
}

.image-2-4 {
  background-image: url('@/assets/images/fixed/10.png');
}

.image-2-5 {
  background-image: url('@/assets/images/fixed/11.png');
}

.image-2-6 {
  background-image: url('@/assets/images/fixed/12.png');
}

.image-3-1 {
  background-image: url('@/assets/images/fixed/13.png');
}

.image-3-2 {
  background-image: url('@/assets/images/fixed/14.png');
}

.image-3-3 {
  background-image: url('@/assets/images/fixed/15.png');
}

.image-3-4 {
  background-image: url('@/assets/images/fixed/16.png');
}

.image-3-5 {
  background-image: url('@/assets/images/fixed/17.png');
}

.image-3-6 {
  background-image: url('@/assets/images/fixed/18.png');
}
</style>
