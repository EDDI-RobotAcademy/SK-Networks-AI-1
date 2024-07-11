export interface KafkaTestState {
    kafkaTestData: KafkaTestItem | null
    isRequest: boolean
}

export interface KafkaTestItem {
    message: string
    data: any
    title: string
}

const state: KafkaTestState = {
    kafkaTestData: null,
    isRequest: false,
}

export default state