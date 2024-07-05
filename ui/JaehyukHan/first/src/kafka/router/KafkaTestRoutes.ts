import KafkaTestPage from "../pages/KafkaTestPage.vue";

const KafkaTestRoutes = [
    {
        path:'/kafka/test',
        name: 'KafkaTestPage',
        components:{
            default: KafkaTestPage
        },
    },
]

export default KafkaTestRoutes