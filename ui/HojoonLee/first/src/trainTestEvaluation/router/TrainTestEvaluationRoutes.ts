import TrainTestEvaluationResultPage from "@/trainTestEvaluation/pages/TrainTestEvaluationResultPage.vue"

const TrainTestEvaluationRoutes = [
    {
        path: '/train-test-evaluation-result', // "localhost8080:/train-test-evaluation-result" 하면 vue에서 구현한 화면이 나온다.
        name: 'TrainTestEvaluationResultPage',
        component : TrainTestEvaluationResultPage
    }
]

export default TrainTestEvaluationRoutes