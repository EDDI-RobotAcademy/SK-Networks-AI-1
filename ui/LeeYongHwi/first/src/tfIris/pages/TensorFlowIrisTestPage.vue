<template>
    <v-container>
        <v-form @submit.prevent="submitForm">
            <v-text-field label="Sepal Length" v-model="form.sepal_length" type="number"/>
            <v-text-field label="Sepal Width" v-model="form.sepal_width" type="number"/>
            <v-text-field label="Petal Length" v-model="form.petal_length" type="number"/>
            <v-text-field label="Petal Width" v-model="form.petal_width" type="number"/>
            <v-btn type="submit" color="primary">Predict</v-btn>
        </v-form>
        <v-btn @click="trainModel" color="secondary">Train Model</v-btn>
        <div if="prediction">
            <!-- vue 자체가 가지고 있는 데이터를 불러올 때 {{  }} 씀 -->
            <p>Predicted Class: {{ predicted_class }}</p> 
            <p>Prediction: {{ prediction }}</p> 
        </div>
    </v-container>
</template>

<script>
import axios from 'axios'
// import * as d3 from 'd3'

export default {
    data () {
        return {
            form: {
                sepal_length: 4.8,
                sepal_width: 3.4,
                petal_length: 1.3,
                petal_width: 0.17,
            },
            prediction: null,
        }
    },
    methods: {
        async submitForm () {
            try {
                const {
                    sepal_length,
                    sepal_width,
                    petal_length,
                    petal_width,
                } = this.form

                const response = await axios.post('http://localhost:33333/tf-predict', {
                    sepal_length,
                    sepal_width,
                    petal_length,
                    petal_width,
                })
                console.log('prediction:', response.data)
                this.prediction = response.data.prediction
                this.predicted_class = response.data.predicted_class
            } catch (error) {
                alert('모델이 훈련되지 않았습니다.')
            }
        },
        async trainModel () {
            await axios.get('http://localhost:33333/tf-train')
            alert('모델 훈련이 완료되었습니다.')
        }
    }
}
</script>