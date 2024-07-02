import OrderListPage from '@/order/pages/read/OrderReadPage.vue'

const CartRoutes = [
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

export default CartRoutes