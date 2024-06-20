import LogisticRegressionResultPage from "@/logisticRegression/pages/LogisticRegressionResultPage.vue"

const LogisticRegressionRoutes = [
    {
        path: '/logistic-regression', // "localhost8080:/logistic-regression" 하면 vue에서 구현한 화면이 나온다.
        name: 'LogisticRegressionResultPage',
        component : LogisticRegressionResultPage
    }
]

export default LogisticRegressionRoutes