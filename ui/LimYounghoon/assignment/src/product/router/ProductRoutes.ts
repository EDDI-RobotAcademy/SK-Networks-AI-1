import ProductListPage from "@/product/pages/list/ProductListPage.vue"
import ProductRegisterPage from "@/product/pages/register/ProductRegisterPage.vue"

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
]

export default ProductRoutes