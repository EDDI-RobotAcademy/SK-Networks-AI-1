import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import BoardRoutes from '@/board/router/BoardRoutes'
import ProductRoutes from '@/product/router/ProductRoutes'
import HomeRoutes from '@/home/router/HomeRoutes'
import AccountRoutes from '@/account/router/AccountRoutes'
import AuthenticationRoutes from '@/authentication/router/AuthenticationRoutes'
import LogisticRegressionRoutes from '@/logisticRegression/router/LogisticRegressionRoutes'
import PolynomialRegressionRoutes from '@/polynomialRegression/router/PolynomialRegressionRoutes'
import ExponentialRegressionRoutes from '@/exponentialRegression/router/ExponentialRegressionRoutes'
import PostRoutes from '@/post/router/PostRoutes'

const routes: Array<RouteRecordRaw> = [
  ...HomeRoutes,
  ...BoardRoutes,
  ...ProductRoutes,
  ...AccountRoutes,
  ...AuthenticationRoutes,
  ...LogisticRegressionRoutes,
  ...PolynomialRegressionRoutes,
  ...ExponentialRegressionRoutes,
  ...PostRoutes
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router