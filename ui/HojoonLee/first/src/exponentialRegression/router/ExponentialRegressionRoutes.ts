import ExponentialRegressionResultPage from "@/exponentialRegression/pages/ExponentialRegressionResultPage.vue"

const ExponentialRegressionRoutes = [
    {
        path: '/exponential-regression-result', // "localhost8080:/logistic-regression" 하면 vue에서 구현한 화면이 나온다.
        name: 'ExponentialRegressionResultPage',
        component : ExponentialRegressionResultPage
    }
]

export default ExponentialRegressionRoutes