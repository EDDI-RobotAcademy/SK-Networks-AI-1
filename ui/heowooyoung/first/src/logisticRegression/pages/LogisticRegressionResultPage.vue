<template>
    <v-container class="chart-container">
        <h2>Logistic Regression Chart</h2>
        <p>Accuary: {{  accuracy }}</p>
        <div ref="chartContainer">
            <svg ref="svg" :viewBox="`0 0 ${svgWidth} ${svgHeight}`" preserveAspectRatio="xMidYMid meet"/>
        </div>
    </v-container>
</template>

<script>
import axiosInstance from '@/utility/axiosInstance';


export default {
    data () {
        return {
            accuracy: 0,
            X: [],
            y: [],
            x_values: [],
            y_values: [],
            svgWidth: 0,
            svgHeight: 0,
            margin: {},
            resizeTimer: null,
        }
    },
    mounted () {
        this.fetchLogisticRegressionData()
    },
    methods: {
        async fetchLogisticRegressionData () {
            try {
                const response = await axiosInstance.fastapiAxiosInst.get('/logistic-regression')
                console.log('result: ', response.data)
            } catch (error) {
                console.error('로지스틱 회귀 분석 중 에러 발생: ', error)
            }
        }
    }
}
</script>

<style scoped>
.chart-container {
    margin: auto
}
</style>