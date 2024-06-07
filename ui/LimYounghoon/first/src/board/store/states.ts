export interface BoardState {
    // 대표적인 예이다.
    // boards는 복수형이므로 배열 타입 (리스트를 의미하고 있음)
    // '변수: 타입'의 형태로 표기한다.
    boards: Board[];
    board: Board | null;
}

// TypeScript는 특이한 형식이 있다.
// 어떤 형식이냐 ? python을 할 때 제일 불편했던 것은 무엇인가 ?
// TypeScript에서는 다시 타입을 명시하게 된다.
export interface Board {
    boardId: number;
    title: string;
    writer: string;
    regDate: string;
    updDate: string;
}

// 좋은 점도 있지만 단점도 있다.
// 뭐냐 ? 너무 엄격하다.
// 너무 엄격하다 못해 컴파일이 안됨.
const state: BoardState = {
    boards: [],
    board: null,
};

export default state;
