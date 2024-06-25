import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

import BoardRoutes from '@/board/router/BoardRoutes'
import ProductRoutes from '@/product/router/ProductRoutes'
import HomeRoutes from '@/home/router/homeRoutes'
import AccountRoutes from '@/account/router/AccountRoutes'
import AuthenficationRoutes from '@/authentication/router/AuthenticationRouter'
import LogisticRegressionRoutes from '@/logisticRegression/router/LogisticRegressionRoutes'
import TrainTestEvaluationRoutes from '@/trainTestEvaluation/router/TrainTestEvaluationRoutes'
import PolynomialRegressionRoutes from '@/polynomialRegression/router/PolynomialRegressionRoutes'
import ExponentialRegressionRoutes from '@/exponentialRegression/router/ExponentialRegressionRoutes'
import RandomForestRoutes from '@/random_forest/router/RandomForestRoutes'
import CartRoutes from '@/cart/router/CartRoutes'
import PostRoutes from '@/post/router/PostRoutes'




const routes: Array<RouteRecordRaw> = [
  // 항상 도메인의 router 추가했으면 main router 에도 추가해줘야함
  ...HomeRoutes,
  ...BoardRoutes,
  ...ProductRoutes,
  ...AccountRoutes,
  ...AuthenficationRoutes, 
  ...LogisticRegressionRoutes,
  ...TrainTestEvaluationRoutes,
  ...PolynomialRegressionRoutes,
  ...ExponentialRegressionRoutes,
  ...RandomForestRoutes,
  ...CartRoutes,
  ...PostRoutes,
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
