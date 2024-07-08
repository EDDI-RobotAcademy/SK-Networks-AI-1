import OrderReadPage from '@/order/pages/read/OrderReadPage.vue'
import OrderListPage from '@/order/pages/list/OrderListPage.vue'

const OrderRoutes = [
    {
        path: '/order/list',
        name: 'OrderListPage',
        components: {
            default: OrderListPage
        },
    },
    {
        path: '/order/read/:orderId',
        name: 'OrderReadPage',
        components: {
            default: OrderReadPage
        },
        props: {
            default: true
        }
    },
]

export default OrderRoutes