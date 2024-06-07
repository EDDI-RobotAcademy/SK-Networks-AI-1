import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BoardRoutes from '@/board/router/BoardRoutes'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/', // root를 의미. 입력했을때 HomeView.vue가 실행되는 것. 홈페이지의 메인 페이지부분
    name: 'home',
    component: HomeView
  },
  ...BoardRoutes  
]
// 실제 자바스크립트이든 typescript이든 spread 문법을 가지고 있습니다.
// 내부에 가지고 있는 내용을 그대로 분산시켜서 뒤에 붙이는 작업을 말합니다.
// 그러므로  ...BoardRoutes 내에 있는 모든 내용을 뒤에 붙입니다.

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
