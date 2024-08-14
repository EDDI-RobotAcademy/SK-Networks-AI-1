import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

import BoardRoutes from '@/board/router/BoardRoutes'
import ProductRoutes from '@/product/router/ProductRoutes'
import HomeRoutes from '@/home/router/HomeRoutes'
import AccountRoutes from '@/account/router/AccountRoutes'
import AuthenticationRoutes from '@/authentication/router/AuthenticationRoutes'
import D3PlotRoutes from '@/d3plot/router/D3PlotRoutes'
import LogisticRegressionRoutes from '@/logisticRegression/router/LogisticRegressionRoutes'
import TrainTestEvaluationRoutes from '@/trainTestEvaluation/router/TrainTestEvaluationRoutes'
import CartRoutes from "@/cart/router/CartRoutes";
import PolynomialRegressionRoutes from '@/polynomialRegression/router/PolynomialRegressionRoutes'
import ExponentialRegressionRoutes from '@/exponentialRegression/router/ExponentialRegressionRoutes'
// import WordCloudRoutes from "@/wordCloud/router/WordCloudRoutes";
// import NaturalLanguageProcessingRoutes from "@/naturalLanguageProcessing/router/NaturalLanguageProcessingRoutes";
import RandomForestRoutes from '@/randomForest/router/RandomForestRoutes'
import PostRoutes from '@/post/router/PostRoutes'
import KmeansRoutes from "@/kmeans/router/KmeansRoutes";
import TensorFlowIrisTestRoutes from '@/tfIris/router/TensorFlowIrisTestRoutes'
import OrderRoutes from '@/order/router/OrderRoutes'
import KafkaTestRoutes from "@/kafka/router/KafkaTestRoutes";
// import FileS3TestRoutes from "@/fileS3/router/FileS3TestRoutes";
import PrincipalComponentAnalysisRoutes from '@/principalComponentAnalysis/router/PrincipalComponentAnalysisRoutes'
import GatherEverythingRoutes from '@/gatherEverything/router/GatherEverythingRoutes'

const routes: Array<RouteRecordRaw> = [
  ...HomeRoutes,
  // 실제 Javascript 던 Typescript 던 spread 문법을 가지고 있습니다.
  // 내부에 가지고 있는 내용을 그대로 분산시켜서 뒤에 붙이는 작업입니다.
  // 그러므로 ...BoardRoutes 는 BoardRoutes 내에 있는 모든 내용을 뒤에 붙입니다.
  ...BoardRoutes,
  ...ProductRoutes,
  ...AccountRoutes,
  ...AuthenticationRoutes,
  ...D3PlotRoutes,
  ...LogisticRegressionRoutes,
  ...TrainTestEvaluationRoutes,
  ...CartRoutes,
  ...PolynomialRegressionRoutes,
  ...ExponentialRegressionRoutes,
  // ...WordCloudRoutes,
  // ...NaturalLanguageProcessingRoutes,
  ...RandomForestRoutes,
  ...PostRoutes,
  ...KmeansRoutes,
  ...TensorFlowIrisTestRoutes,
  ...OrderRoutes,
  ...KafkaTestRoutes,
  // ...FileS3TestRoutes,
  ...PrincipalComponentAnalysisRoutes,
  ...GatherEverythingRoutes,
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router