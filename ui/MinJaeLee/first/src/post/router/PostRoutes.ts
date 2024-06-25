import PostListPage from "../pages/list/PostListPage.vue"
import PostRegisterPage from "../pages/register/PostRegisterPage.vue"
import PostReadPage from "../pages/read/PostReadPage.vue"
const ProductRoutes = [
    {
        path: '/post/list',
        name: 'PostListPage',
        component: PostListPage,
    },
    {
        path: '/post/register',
        name: 'PostRegisterPage',
        component: PostRegisterPage,
    },
    {
        path: '/post/read/:id',
        name: 'PostReadPage',
        components: {
            default: PostReadPage,
        },
        props: {
            default: true
        },
    },
]

export default ProductRoutes