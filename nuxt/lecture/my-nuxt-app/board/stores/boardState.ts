export const boardState = () => ({
    boardList: [] as Array<{ 
        boardId: number, 
        title: string, 
        writer: string, 
        regDate: string 
    }>
})