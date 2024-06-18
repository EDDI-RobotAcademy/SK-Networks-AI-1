import ProductListPage from "@/product/pages/list/ProductListPage.vue"
import ProductRegisterPage from "@/product/pages/register/ProductRegisterPage.vue"
import ProductReadPage from "@/product/pages/read/ProductReadPage.vue"

const ProductRoutes = [
    {
        path: '/product/list',
        name: 'ProductListPage',
        component: ProductListPage,
    },
    {
        path: '/product/register',
        name: 'ProductRegisterPage',
        component: ProductRegisterPage,
    },
    {
        path: '/product/read/:productId',
        name: 'ProductReadPage',
        components: {
            default: ProductReadPage
        },
        props: {
            default: true
        },
    },
]

export default ProductRoutes