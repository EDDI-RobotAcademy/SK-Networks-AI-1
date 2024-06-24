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
        // productId를 활용하기 때문에 Vue끼리 충돌하는 것 방지 (ProductReadPage, Productlistpage)
        // list page안에 read page로 구성되어 있기 때문에 Vue는 어느 페이지를 먼저보여줘야할지 혼란에 빠짐
        // 이 우선순위를 정해주는 것이 아래처럼 만들어준다.
        components: {
            default : ProductReadPage
        },
        props: {
            default : true
        }
    },
]

export default ProductRoutes