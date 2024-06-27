import PostListPage from "@/post/pages/list/PostListPage.vue"
import PostRegisterPage from "@/post/pages/register/PostRegisterPage.vue"
import PostReadPage from "@/post/pages/read/PostReadPage.vue"

const PostRoutes = [
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

export default PostRoutes