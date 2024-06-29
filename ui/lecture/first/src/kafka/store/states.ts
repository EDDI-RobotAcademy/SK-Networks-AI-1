export interface KafkaTestState {
    kafkaTestData: KafkaTestItem | null;
}

export interface KafkaTestItem {
    message: string;
    data: any;
    title: string;
}

const state: KafkaTestState = {
    kafkaTestData: null
};

export default state;
