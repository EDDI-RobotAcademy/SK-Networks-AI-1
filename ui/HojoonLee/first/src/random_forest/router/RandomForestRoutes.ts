import RandomForestResultPage from "@/random_forest/pages/RandomForestResultPage.vue"

const RandomForestRoutes = [
    {
        path: '/random-forest-result', // "localhost8080:/logistic-regression" 하면 vue에서 구현한 화면이 나온다.
        name: 'RandomForestResultPage',
        component : RandomForestResultPage
    }
]

export default RandomForestRoutes