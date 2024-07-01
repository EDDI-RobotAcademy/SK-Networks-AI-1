<template>
    <v-container class="chart-container">
        <h2>Exponential Regression Analysis</h2>
        <v-row>
            <v-col>
                <div ref="chart"/>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axiosInstance from '@/utility/axiosInstance';
import * as d3 from 'd3'
import { ref, onMounted } from 'vue'

export default {
    setup () {
        const chart = ref(null)
        const originalData = ref([])
        const predictedData = ref([])

        const fetchExponentialRegressionData = async () => {
            try {
                const response = await axiosInstance.fastapiAxiosInst.get('/exponential-regression')
                const data = await response.data
                // 이렇게 fetch를 하게 되면 문제가 생김
                // const response = await fetch('http://localhost:33333/exponential-regression')
                // const data = await response.json()
                
                originalData.value = data.original_data
                console.log('originalData:', originalData.value)

                predictedData.value = data.predicted_data
            } catch (error) {
                console.error('exponential 회귀 분석 데이터 확보 중 에러 발생:', error)
            }
        }
        const drawChart = () => {
            const margin = { top: 20, right: 20, bottom: 30, left: 40 }
            const width = 960 - margin.left - margin.right
            const height = 500 - margin.top - margin.bottom

            const x = d3.scaleLinear().range([0, width])
            const y = d3.scaleLinear().range([height, 0])

            const line = d3.line()
                            .x(d => x(d[0]))
                            .y(d => y(d[1]))

            const svg = d3.select(chart.value).append('svg')
                            .attr('width', width + margin.left + margin.right)
                            .attr('height', height + margin.top + margin.bottom)
                            .append('g')
                            .attr('transform', `translate(${margin.left}, ${margin.top})`)

            x.domain(d3.extent(originalData.value, d => d[0]))
            y.domain([0, d3.max(originalData.value, d => d[1])])

            svg.append('g')
                    .attr('class', 'x axis')
                    .attr('transform', `translate(0, ${height})`)
                    .call(d3.axisBottom(x))

            svg.append('g')
                    .attr('class', 'y axis')
                    .call(d3.axisLeft(y))

            // 채우기 주의!
            svg.append('path')
                    .datum(originalData.value)
                    .attr('class', 'line')
                    .attr('d', line)
                    .style('stroke', 'steelblue')
                    .style('fill', 'none')

            svg.append('path')
                    .datum(predictedData.value)
                    .attr('class', 'line')
                    .attr('d', line)
                    .style('stroke', 'red')
                    .style('fill', 'none')

            // 채우기 이슈가 있어서 수정 필요함
            svg.selectAll('.dot')
                    .data(originalData.value)
                    .enter().append('circle')
                    .attr('class', 'dot')
                    .attr('cx', d => x(d[0]))
                    .attr('cy', d => y(d[1]))
                    .attr('r', 3)
                    .style('fill', 'steelblue')
        }

        onMounted(async () => {
            await fetchExponentialRegressionData()
            drawChart()
        })

        // 원래 데이터 설정할 때 data () { return: { chart }}
        // 대략 위와 같은 느낌이었음
        // 그러나 setup() 내에서 사용할 때 data를 직접 표기하지 않고
        // return에 배치해서 사용할 데이터나 refs를 맵핑한다 보면 됨
        return { chart }
    }
}
</script>