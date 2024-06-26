<template>
    <v-container>
        <v-form @submit.prevent="submitForm">
            <v-text-field label="Sepal Length" v-model="form.sepal_length" type="number" />
            <v-text-field label="Sepal Width" v-model="form.sepal_width" type="number" />
            <v-text-field label="Petal Length" v-model="form.petal_length" type="number" />
            <v-text-field label="Petal Width" v-model="form.petal_width" type="number" />
            <v-btn type="submit" color="primary">Predict</v-btn>
        </v-form>
        <v-btn @click="trainModel" color="secondary">Train Model</v-btn>
    </v-container>
</template>

<script>
import axios from 'axios'
// import * as d3 from 'd3'

export default {
    data() {
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
        async submitForm() {
            try {
                const formData = new FormData()
                formData.append('sepal_length', this.form.sepal_length)
                formData.append('sepal_width', this.form.sepal_width)
                formData.append('petal_length', this.form.petal_length)
                formData.append('petal_width', this.form.petal_width)

                const response = await axios.get('http://localhost:33333/tf-predict', this.form)
            } catch (error) {
                alert('훈련된 모델 존재하지 않음')
            }
        },
        async trainModel() {
            await axios.get('http://localhost:33333/tf-train')
            alert('딥러닝 모델 훈련 완료')
        }
    }
}
</script>