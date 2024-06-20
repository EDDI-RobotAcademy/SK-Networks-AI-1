import PolynomialRegressionResultPage from "@/polynomialRegression/pages/PolynomialRegressionReulstPage.vue"

const PolynomialRegressionRoutes = [
    {
        path: '/polynomial-regression-result', // "localhost8080:/logistic-regression" 하면 vue에서 구현한 화면이 나온다.
        name: 'PolynomialRegressionResultPage',
        component : PolynomialRegressionResultPage
    }
]

export default PolynomialRegressionRoutes