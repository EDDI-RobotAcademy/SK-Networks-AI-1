<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <h1>Natural Language Processing App</h1>
            </v-col>
            <v-col cols="12">
                <v-btn @click="loadData" :loading="loadingData" color="primary" class="ma-2">Load Data</v-btn>
                <v-btn @click="trainModel" :loading="trainingModel" color="primary" class="ma-2">Train Model</v-btn>
            </v-col>
            <v-col cols="12">
                <v-btn @click="predictSentiment('This movie was fantastic!')" :loading="predicting" color="secondary" class="ma-2">Predict: Fantastic Movie</v-btn>
                <v-btn @click="predictSentiment('I did not like this movie at all.')" :loading="predicting" color="secondary" class="ma-2">Predict: Disliked Movie</v-btn>
                <v-btn @click="predictSentiment('It was an average film.')" :loading="predicting" color="secondary" class="ma-2">Predict: Average Film</v-btn>
                <v-btn @click="predictSentiment('The acting was great but the story was boring.')" :loading="predicting" color="secondary" class="ma-2">Predict: Mixed Feelings</v-btn>
                <v-btn @click="predictSentiment('I would not recommend this movie.')" :loading="predicting" color="secondary" class="ma-2">Predict: Not Recommend</v-btn>
            </v-col>
            <v-col cols="12">
                <v-alert v-if="responseMessage" :type="alertType" dismissible>
                    {{ responseMessage }}
                </v-alert>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            loadingData: false,
            trainingModel: false,
            predicting: false,
            responseMessage: '',
            alertType: 'info',
        };
    },
    methods: {
        async loadData() {
            this.loadingData = true;
            this.responseMessage = '';
            try {
                const response = await axios.get('http://localhost:33333/load-data');
                this.responseMessage = response.data.message;
                this.alertType = 'success';
            } catch (error) {
                this.responseMessage = error.response?.data?.detail || 'Error loading data';
                this.alertType = 'error';
            } finally {
                this.loadingData = false;
            }
        },
        async trainModel() {
            this.trainingModel = true;
            this.responseMessage = '';
            try {
                const response = await axios.get('http://localhost:33333/train-model');
                this.responseMessage = response.data.message;
                this.alertType = 'success';
            } catch (error) {
                this.responseMessage = error.response?.data?.detail || 'Error training model';
                this.alertType = 'error';
            } finally {
                this.trainingModel = false;
            }
        },
        async predictSentiment(text) {
            this.predicting = true;
            this.responseMessage = '';
            try {
                const response = await axios.get('http://localhost:33333/predict', {
                    params: { text },
                });
                this.responseMessage = `Sentiment: ${response.data.sentiment}`;
                this.alertType = 'success';
            } catch (error) {
                this.responseMessage = error.response?.data?.detail || 'Error predicting sentiment';
                this.alertType = 'error';
            } finally {
                this.predicting = false;
            }
        },
    },
};
</script>

<style>
.ma-2 {
    margin: 0.5rem;
}
</style>
