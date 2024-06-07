export interface BoardState {

    //아래 주석의 대표적인 예가 이것임
    //boards는 복수형이므로 배열 타입(리스트를 의미하고 있음)
    //'변수:타입'형태로 표기함
    boards: Board[]
    board: Board | null
}

//TypeScript는 특이한 형식이 있습니다.
//어떤 형식이냐? 파이썬을 할때 제일 불편했던 것은 무엇인가요?
//TypeScript에서는 다시 타입을 명시하게 됩니다.

export interface Board {
    boardId: number
    title: string
    writer: string
    content: string
    regDate: string
    updDate: string
}

const state: BoardState = {
    boards: [],
    board: null
}

//좋은 점도 있지만 단점도 있다
//단점은 너무 엄격하다는 것이다.
//너무 엄격하기 때문에 컴파일이 안된다.
export default state