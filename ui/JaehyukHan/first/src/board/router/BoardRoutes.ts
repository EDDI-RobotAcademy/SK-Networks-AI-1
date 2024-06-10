import BoardListPage from "@/board/pages/list/BoardListPage.vue"
import BoardRegisterPage from "@/board/pages/register/BoardRegisterPage.vue"
import BoardReadPage from "@/board/pages/read/BoardReadPage.vue"

const BoardRoutes = [
    {
        path: '/board/list',
        name: 'BoardListPage',
        component: BoardListPage,
    },
    {
        path: '/board/register',
        name: 'BoardRegisterPage',
        component: BoardRegisterPage,
    },
    {
        path: '/board/read/:boardId',
        name: 'BoardReadPage',
        components: {
            default: BoardReadPage,
        },
        props: {
            default: true
        }
    }
]

export default BoardRoutes
