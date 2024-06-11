import BoardListPage from "@/board/pages/list/BoardListPage.vue"
import BoardRegisterPage from "@/board/pages/register/BoardRegisterPage.vue"
import BoardReadPage from "@/board/pages/read/BoardReadPage.vue"
import BoardModifyPage from "@/board/pages/modify/BoardModifyPage.vue"

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
        // 가변인자
        path: '/board/read/:boardId',
        name: 'BoardReadPage',
        components: {
            default: BoardReadPage,
        },
        // 프롭스 설정을 해야 파라미터로 넘길 수 있음
        props: {
            default: true
        }
    },
    {
        path: '/board/modify/:boardId',
        name: 'BoardModifyPage',
        components: {
            default: BoardModifyPage,
        },
        props: {
            default: true
        }
    },
]

export default BoardRoutes