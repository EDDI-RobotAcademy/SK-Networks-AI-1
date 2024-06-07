export interface BoardState { // 파이썬의 ABC abstractmethod와 역할이 같습니다.
    // 대표적인  예이기도 함
    // boards는 복수형이므로 배열 타입 (list를 의미하고 있음)
    // '변수: 타입' 형태로 표기
    boards: Board[]
    board: Board | null
}

// TypeScript(.ts)는 특이한 형식이 있습니다.
// TypeScript에서는 다시 타입을 명시하게 됩니다. 

export interface Board {
    boardId: number // type 명시
    title: string
    writer: string
    content: string
    regDate: string
    update: string
}

// 위의 export interface는 외부로 방출시켰다. 새로운 타입을 만든 것 like ABC?

// 좋은 점도 있지만 단점이 있다면, 너무 엄격하다는 것입니다.
// 엄격하다 못해 컴파일이 안됩니다. 타입을 안 맞추면 절대 실행되지 않는다는 의미입니다.

const state : BoardState ={ // 상수값인 state를 만들건데, BoardState 타입이다
    boards: [],
    board: null
}

export default state