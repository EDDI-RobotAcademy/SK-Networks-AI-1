import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import BoardRoutes from '@/board/router/BoardRoutes'
import ProductRoutes from '@/product/router/ProductRoutes'
import HomeRoutes from '@/home/router/HomeRoutes'
import AccountRoutes from '@/account/router/AccountRoutes'
import AuthenticationRoutes from '@/authentication/router/AuthenticationRoutes'
import LogisticRegressionRoutes from '@/logisticRegression/router/LogisticRegressionRoutes'
import TrainTestEvaluationRoutes from '@/trainTestEvaluation/router/TrainTestEvaluationRoutes'
import PolynomialRegressionRoutes from '@/polynomialRegression/router/PolynomialRegressionRoutes'

const routes: Array<RouteRecordRaw> = [
  ...HomeRoutes,
  // 실제 javascript 던 Typescript 던 spread 문법을 가지고 있습니다.
  // 내부에 가지고 있는 내용을 그대로 분산시켜서 뒤에 붙이는 작업입니다.
  // 그러므로 ...BoardRoutes
  ...BoardRoutes,
  ...ProductRoutes,
  ...AccountRoutes,
  ...AuthenticationRoutes,
  ...AccountRoutes,
  ...LogisticRegressionRoutes,
  ...TrainTestEvaluationRoutes,
  ...PolynomialRegressionRoutes
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
