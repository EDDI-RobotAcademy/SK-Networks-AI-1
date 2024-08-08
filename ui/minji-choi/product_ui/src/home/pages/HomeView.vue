<template>
  <div>
    <div class="background">
      <div class="stars"></div>
      <v-row justify="center" align="center" style="height: 100vh; position: relative;">
        <v-col cols="12">
          <!-- v-img 컴포넌트를 사용하여 이미지를 삽입 -->
          <v-img
            src="@/assets/images/fixed/brd.png"
            height="100%"  
            contain  
          ></v-img>
          <!-- 이미지 위에 텍스트를 추가 -->
          <div class="text-overlay">
            <span class="main-text">나는 춘식이</span>
            <br><br>
            <span class="sub-text">
              "나는 춘식이"는 당신만의 감정, 스타일, 그리고 세계관을 담아낼 수 있는 퍼스널 이모티콘 발견의 기회를 제공합니다.
              <br>
              비대면 소통이 증가함에 따라, 우리에게는 언어를 넘어서서 감정과 생각을 전달할 수 있는 방법이 필요합니다.
            </span>
            <br><br>
            <span class="sub-text-2">
              이모티콘은 언어를 넘어선 소통 방법입니다. 
            </span>   
            <br>      
            <span class="sub-text">
              유명 이모티콘 "춘식이"에서 영감을 받아 이모티콘이 되는 나, "나는 춘식이"가 탄생했습니다.
              당신이 자신을 파악할 수 있도록 
              <br>다양한 이모티콘들을 모아두었습니다.
            </span>
            <br><br>
            <span class="sub-text">
              성별, 연령, 혹은 취향에 맞는 다양한 선택지를 통해 당신이 원하는 이모티콘을 찾아보세요. <br>당신을 나타내는 그 하나의 작은 표현이 될 것입니다.
            </span>
            <br><br>
            <span class="sub-text">
              "나는 춘식이"는 단순히 이모티콘을 판매하는 곳 이상입니다. <br>당신의 정체성과 감정을 자유롭게 표현하세요.
              온라인, 오프라인 그 어느 곳에서도 당신은 존재합니다. 지금 당신의 이모티콘을 찾아보세요!
            </span>
            <!-- 버튼 추가 -->
            <br><br>
            <div class="button-container">
              <v-img src="@/assets/images/fixed/button.png" alt="Button" class="button-image" @click="goToProductList"/>
            </div>
          </div>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default {
  data () {
    return {

    }
  },
  methods: {
    goToProductList() {
        // this.$router.push({ name: 'ProductListPage' }); 
        console.log('페이지 이동')
    }

}
};
</script>

<style scoped>
.background {
  position: relative; /* 자식 요소의 위치를 상대적으로 설정 */
  background-color: #fff; /* 배경 이미지가 로딩되기 전에 보일 색상 */
  overflow: hidden; /* 자식 요소들이 배경을 벗어나지 않도록 함 */
}

.stars {
  width: 200%;
  height: 200%;
  background: url('https://www.transparenttextures.com/patterns/stardust.png');
  position: absolute;
  top: -50%;
  left: -50%;
  z-index: 1;
  animation: twinkling 60s infinite;
}

@keyframes twinkling {
  0% { background-position: 0 0; }
  100% { background-position: -10000px 5000px; }
}

.text-overlay {
  position: absolute; /* 절대 위치로 설정하여 이미지 위에 겹쳐질 수 있도록 함 */
  top: 50%; /* 화면 상단에서 세로 중앙으로 위치 */
  left: 37%; /* 왼쪽 여백 조정 */
  transform: translate(-50%, -50%); /* 중앙 정렬을 위한 transform */
  z-index: 10; /* 다른 요소들보다 위에 표시될 수 있도록 z-index 설정 */
  text-align: left; /* 텍스트를 왼쪽 정렬 */
  color: white; /* 텍스트 색상 */
  font-size: 24px; /* 메인 텍스트 크기 */
  font-weight: bold; /* 메인 텍스트 굵기 */
  line-height: 1.5; /* 줄간격 설정 */
}

.main-text {
  font-size: 48px; /* 메인 텍스트 크기 */
  font-weight: bold; /* 메인 텍스트 굵기 */
}

.sub-text {
  font-size: 16px; /* 서브 텍스트 크기 */
  font-weight: normal; /* 서브 텍스트 굵기 */
}

.sub-text-2 {
  font-size: 20px; /* 서브 텍스트 크기 */
  font-weight: bold; /* 서브 텍스트 굵기 */
}

.button-container {
  text-align: center; /* 버튼을 가운데 정렬 */
}

.button-image {
  width: 100px; /* 버튼 이미지의 너비 */
  height: auto; /* 비율을 유지한 채 높이를 자동으로 조정 */
  cursor: pointer; /* 버튼에 마우스를 올렸을 때 포인터로 변경 */
}
</style>
