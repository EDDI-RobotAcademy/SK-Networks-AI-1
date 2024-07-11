// 카프카한테 요청을 보내면 어떤식으로 리턴을 줄지 구현하는 부분
// 그러므로 일반적인 states 부분들과는 구성이 다름

export interface KafkaTestState {
    kafkaTestData: KafkaTestItem | null; // KafkaTestData는 KafkaTestItem으로 구성
    isRequest: boolean // 카프카한테 요청 보냈냐 여부 확인
}

// 실제 데이터 내부는 이런 것들을 다뤄줄 것임
export interface KafkaTestItem {
    message: string;
    data: any;
    title: string;
}

const state: KafkaTestState = {
    kafkaTestData: null,
    isRequest: false,
}

export default state