export interface BoardState {
    // 타입을 명시하는 대표적인 예
    // boards는 복수형이므로 배열 타입(리스트를 의마하고 있음)
    // '변수: 타입' 형태로 표기함
    boards: Board[]
    board: Board | null
}

// TypeScript는 특이한 형식이 있습니다.
// 어떤 형식이냐? python을 할 때 제일 불편했던 것은 무엇인가요?
// Python이나 JavaScript에서 마음대로 타입이 바뀌는 에러가 종종 발생
// 이러한 경우 에러를 찾기도 힘들고 시간이 많이 소요됩니다.
// 그래서 TypeScript에서는 다시 타입을 명시하게 됩니다.
export interface Board {
    boardId: number
    title: string
    writer: string
    content: string
    regDate: string
    updDate: string
}

// 타입을 지정해주는 것이 좋은 점도 있지만 단점이 있습니다.
// 뭐냐? 너무 엄격하다.
// 너무 엄격하다 못해 컴파일이 안됨
const state: BoardState = {
    boards: [],
    board: null
}

export default state