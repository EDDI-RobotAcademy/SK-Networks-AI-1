<template>
    <V-container>
        <v-from @submit.prevent="submitForm">
            <v-text-field label="Sepal Length" v-model="form.Sepal_length" type="number">
                <v-btn type="submit" color="primary">Predict</v-btn>
            </v-text-field>
        </v-from>
        <v-btn @click="trainModel" color="danger">Train Model</v-btn>
    </V-container>
</template>

<script>
import axios from 'axios'
import * as d3 from 'd3'

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
                const response = await axios.get('http://192.168.0.42:33333/tf-predict', this.form)
            } catch (error) {
                alert('딥러닝 모델이 훈련되지 않았으니 모델부터 훈련시키세요!')
            }
        },

        async trainModel () {
            await axios.get('http://192.168.0.42:33333/tf-train')
            alert('딥러닝 모델 훈련이 완료되었습니다!')
        }
    }
}
</script>