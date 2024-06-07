import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import BoardRoutes from "@/board/router/BoardRoutes";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  // 실제 Javascript던 Typescript던 spread 문법을 가지고 있다.
  // 내부에 가지고 있는 내용을 그대로 분산시켜서 뒤에 붙이는 작업이다.
  // 그러므로 ...BoardRoutes는 boardRoutes 내에 있는 모든 내용을 뒤에 붙인다.
  ...BoardRoutes,
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
