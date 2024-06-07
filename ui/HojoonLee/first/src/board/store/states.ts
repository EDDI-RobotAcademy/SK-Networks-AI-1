// interface : 파이썬의 추상화 클래스와 하는일 동일
export interface BoardState {
    // 대표적인 예이기도 함
    // boards는 복수형이므로 배열 타입 (리스트를 의미하고 있음)
    // '변수: 타입' 형태로 표기함
    boards: Board[]
    board: Board | null
}

// TypeScript는 특이한 형식이 있습니다.
// 어떤 형식이냐? python을 할 때 제일 불편했던 것은 무엇인가요?
// python이 자기 멋대로 type을 해석함
// 이런 문제를 해결하기 위해 TypeScript에서는 다시 타입을 명시하게 됩니다.
// export로 내보낸 순간 여기서 설정한 변수들은 명시적인 type이 됨 
export interface Board{
    boardId: number
    title: string
    writer: string
    content: string
    regDate: string
    updDate: string
}

// state 상수값 >> boards는 텅빈 list로, board는 null로 표현
// 어떤 데이터가 오든 여기 type과 다르다면 빠꾸시키겠다.의 역할로 사용됨
// 단점 : 너무 엄격하다 못해 컴파일이 안 된다. (rust, typescript 환경에서 ..)
const state: BoardState = {
    boards: [],
    board: null
}

export default state