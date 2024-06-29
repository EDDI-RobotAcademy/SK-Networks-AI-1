<template>
    <v-container fluid>
        <h2 class="mb-4">Kafka Test Page</h2>

        <v-card>
            <v-card-text>
                <v-row>
                    <v-col v-if="!kafkaTestData" cols="12">
                        <p>No response yet.</p>
                    </v-col>
                    <v-col v-else cols="12">
                        <p>Response received: {{ kafkaTestData.data.message }}</p>
                    </v-col>
                </v-row>
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" @click="sendRequest">Send Kafka Request</v-btn>
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
        };
    },
    computed: {
        ...mapState(kafkaTestModule, ['kafkaTestData']), // Map the kafkaTestData state from Vuex
    },
    methods: {
        ...mapActions(kafkaTestModule, ['requestKafkaTestDataToFastapi']),
        async sendRequest() {
            try {
                const requestData = {
                    message: 'Hello Kafka!'
                };

                const response = await this.requestKafkaTestDataToFastapi(requestData)
                console.log('Response from Kafka:', response.data);
                this.response = response.data; // Display response in the template
            } catch (error) {
                console.error('Error sending Kafka request:', error);
                this.response = null; // Clear previous response
            }
        }
    }
};
</script>

<style scoped>
/* Add your component styles here */
</style>
