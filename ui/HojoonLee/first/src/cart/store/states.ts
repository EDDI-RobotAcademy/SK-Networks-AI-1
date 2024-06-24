// state 추상화로 선언
export interface CartState {
    cartItemList: CartItem[]
}

// 추상화된 state 내부의 변수에 대한 type들 설정
// product price를 넣으면 시세변동이 반영이 안됨 그러므로 productID만 보고 바뀐 시세를 참조하는 쪽으로 하는 게 좋음
// 실제로 필요한건 productId, token, quantity
export interface CartItem {
    productId: number
    produtName: string
    productPrice: number
    quantity: number
}

const state: CartState = {
    cartItemList: [],
}

export default state