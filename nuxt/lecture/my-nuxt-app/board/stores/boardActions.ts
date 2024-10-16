import * as axiosUtility from "../../utility/axiosInstance"

export const boardActions = {
    async requestBoardListToDjango() {
        const { djangoAxiosInst } = axiosUtility.createAxiosInstances()

        try {
            const response = await djangoAxiosInst.get('/board/list')
            this.boardList = response.data
        } catch (error) {
            console.error('게시글 목록을 불러오는 중 에러가 발생했습니다:', error)
        }
    }
}