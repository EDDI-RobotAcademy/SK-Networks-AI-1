import BoardListPage from "@/board/pages/list/BoardListPage.vue"

const BoardRoutes = [
    {
        path: '/board/list',   // http://localhost:8080/board/list로 들어가게 되는 것
        name: 'BoardListPage',
        component: BoardListPage // 자유게시판으로 쓰일 어떤 게시판 페이지
    }
]
// 외부로 공개
export default BoardRoutes