export interface AuthenticationState {
    // 대표적인 예이기도 함
    // boards는 복수형이므로 배열 타입 (리스트를 의미하고 있음)
    // '변수: 타입' 형태로 표기함
    isAuthenticated: boolean


// 좋은 점도 있지만 단점이 있습니다.
// 뭐냐 ? 너무 엄격하다.
// 너무 엄격하다 못해 컴파일이 안됨
const state: AuthenticationState = {
    isAuthenticated: false
}

export default state