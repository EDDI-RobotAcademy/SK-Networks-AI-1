
import CartListPage from '@/cart/pages/CartListPage.vue'

const CartRoutes = [
    {
        path: '/order/read',
        name: 'CartListPage',
        components: {
            default: CartListPage
        },
    },
]

export default CartRoutes
