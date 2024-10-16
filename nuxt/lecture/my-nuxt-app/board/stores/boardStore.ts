import { defineStore } from "pinia"
import { createAxiosInstances } from "../../utility/axiosInstance"

export const useBoardStore = defineStore('boardStore', {
    state: () => ({
        boardList: [] as Array<{ boardId: number, title: string, writer: string, regDate: string }>
    }),
    actions: {
        async requestBoardListToDjango() {
            const { djangoAxiosInst } = createAxiosInstances()

            try {
                const response = await djangoAxiosInst.get('/board/list')
                this.boardList = response.data
            } catch (error) {
                console.error('게시글 목록을 불러오는 중 에러가 발생했습니다:', error)
            }
        }
    }
})