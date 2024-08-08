<template>
    <v-container fluid>
        <h2 class="mb-4">Kafka Test Page</h2>

        <v-card>
            <v-card-text>
                <v-row>
                    <v-col cols="12">
                        <p>요청상태: {{ requestStatus }}</p>
                    </v-col>
                    <v-col v-if="!kafkaTestData" cols="12">
                        <p>No response yet.</p>
                    </v-col>
                    <v-col v-else cols="12">
                        <p>Response received: {{ kafkaTestData.data.message }}</p>
                    </v-col>
                </v-row>
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" @click="sendRequest">Send kafka Request</v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script>
import { mapActions, mapState } from "vuex";

const kafkaTestModule = 'kafkaTestModule'

export default {
    data() {
        return {
            response: null
        }
    },
    computed: {
        ...mapState(kafkaTestModule, ['kafkaTestData']),
        requestStatus() {
            if (this.response) {
                return `${this.response.status}`
            } else if (this.$store.state.kafkaTestModule.isRequest) {
                return "데이터를 처리 중입니다"
            } else {
                return '아직 요청하지 않았음'
            }
        }
    },
    methods: {
        ...mapActions(kafkaTestModule, ['requestKafkaTestDataToFastapi']),
        async sendRequest() {
            try {
                const requestData = {
                    message: 'Hello Kafka!'
                }

                const response = await this.requestKafkaTestDataToFastapi(requestData)
                console.log('Response from Kafka:', response.data)
                this.response = response.data
            } catch (error) {
                console.error('Error sending Kafka request:', error)
                this.response = null
            }
        }
    }
}
</script>