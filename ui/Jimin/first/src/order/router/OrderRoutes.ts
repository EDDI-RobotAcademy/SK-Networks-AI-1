import OrderReadPage from "../pages/read/OrderReadPage.vue";

const OrderRoutes = [
    {
        path: '/order/read/:orderId',
        name: 'OrderReadPage',
        components: {
            default: OrderReadPage
        },
        props: {
            default: true
        }
    }
]

export default OrderRoutes