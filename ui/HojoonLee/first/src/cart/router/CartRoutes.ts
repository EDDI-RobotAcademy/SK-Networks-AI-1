import CartListPage from '@/cart/pages/CartListPage.vue'

const CartRoutes = [
    {
        path: '/cart/list',
        name: 'CartListPage',
        // 상품 등록하는 쪽에서 장바구니 넘어갈 수 있기 때문에
        // 다른 도메인(product)에서 해당 도메인(cart)으로 이동하게끔 구현하고 싶으면 components로 선언
        components: {
            default: CartListPage
        },
    },
]

export default CartRoutes