import ProductListPage from "@/product/pages/list/ProductListPage.vue"
import ProductRegisterPage from "@/product/pages/register/ProductRegisterPage.vue"
import ProductReadPage from "@/product/pages/read/ProductReadPage.vue"
import ProductModifyPage from "@/product/pages/modify/ProductModifyPage.vue"
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
        path: '/product/product/read/:productId',
        name: 'ProductReadPage',
        components: { // 왜 components? // vue 페이지 안에 vue 페이지가 있는 경우 router의 구조를 변경해야함. read의 경우 list 안에 있음
            default: ProductReadPage,
        },
        props: {
            default: true
        }
    },
    {
        path: '/product/modify/:productId',
        name: 'ProductModifyPage',
        components: { // 왜 components?
            default: ProductModifyPage,
        },
        props: {
            default: true
        }
    },
]

export default ProductRoutes