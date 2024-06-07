import BoardListPage from "../pages/list/BoardListPage.vue";

const BoardRoutes = [
    {
        path: '/board/list',
        name: 'BoardListPage',
        component: BoardListPage,
    }
]

// 위의 내용(BoardRoutes) 외부로 공개
// Board에서 구현할 내용은 Board dir 아래에다 구현하기
export default BoardRoutes