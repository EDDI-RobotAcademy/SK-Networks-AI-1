import CartListPage from '@/cart/pages/CartListPage.vue'

const CartRoutes = [
    {
        path: '/cart/list',
        name: 'CartListPage',
        components: {
            default: CartListPage
        },
    },
]

export default CartRoutes