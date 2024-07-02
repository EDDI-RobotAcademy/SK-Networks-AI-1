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
import KmeansRoutes from '@/kmeans/router/KmeansRoutes'
import CartRoutes from '@/cart/router/CartRoutes'
import TensorFlowIrisTestRoutes from '@/tfIris/router/TensorFlowIrisTestRoutes'
import OrderRoutes from '@/order/router/OrderRoutes'

const routes: Array<RouteRecordRaw> = [
  ...HomeRoutes,
  ...BoardRoutes,
  ...ProductRoutes,
  ...AccountRoutes,
  ...AuthenticationRoutes,
  ...LogisticRegressionRoutes,
  ...PolynomialRegressionRoutes,
  ...ExponentialRegressionRoutes,
  ...PostRoutes,
  ...CartRoutes,
  ...KmeansRoutes,
  ...TensorFlowIrisTestRoutes,
  ...OrderRoutes
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router