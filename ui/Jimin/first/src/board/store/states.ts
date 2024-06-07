export interface BoardState{
    // 대표적인 예이기도 함
    // boards는 복수형이므로 배열 타입 (리스트를 의미하고 있음)
    // '변수: 타입' 형태로 표기함
    // boards는 Board리스트로(복수), board는 단수 혹은 널값
    boards: Board[]
    board: Board | null
}

// TypeScript는 특이한 형식이 있습니다.
// 어떤 형식이냐? python을 할 때 제일 불편했던 것은 무엇인가요?
// python과 마찬가지로 자료형때문에 오류가 나고 그거 찾느라 시간이 오래 걸린다.
// 그래서 type을 명시하도록 하자 해서 나온것이 typescript이다.
// TypeScript에서는 다시 타입을 명시하게 됩니다.

// export interface한 것들은 나 이런 타입을 만들꺼야 이런거 쓸거야 라는 뜻
// python에서 ABC와 비슷한 것
export interface Board{
    boardId: number
    title: string
    writer: string
    content: string
    regDate: string
    updDate: string
}

// 장점도 있지만 단점도 있다.
// 너무 엄격하다는 단점
// 너무 엄격하다 못해 compile이 안된다.
// 타입을 맞추지 못하면 절대 실행을 안시켜준다
const state: BoardState = {
    boards: [],
    board: null
}

export default state