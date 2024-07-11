export interface KafkaTestState {
    kafkaTestData: kafkaTestItem | null;
    isRequest: boolean
}

export interface kafkaTestItem {
    message: string
    data: any
    title: string
}

const state: KafkaTestState = {
    kafkaTestData: null,
    isRequest: false,
}

export default state