<template>
    <v-container>
        <svg ref="svg" :viewBox="`0 0 ${svgWidth} ${svgHeight}`"
                        preserveAspectRatio="xMidYMid meet"/>
    </v-container>
</template>

<script>
import * as d3 from 'd3'
import axiosInstance from '@/utility/axiosInstance';

export default {
    data () {
        return {
            svgHeight: 350,
            svgWidth: 500,
            regressionData: null,
        }
    },
    async created () {
        try {
            const response = await axiosInstance.fastapiAxiosInst.get('/polynomial-regression')
            const data = await response.data
            // const response = await fetch('http://localhost:33333/polynomial-regression')
            // console.log('response', response)
            // const data = await response.json() // promise 부분에서 뭔 소리가 나서 await를 처리해야함 (반드시 데이터를 기다리도록)
            console.log('data:', data)
            this.regressionData = data
            this.drawChart()
        } catch (error) {
            console.error('다항 회귀 데이터 확보 중 에러:', error)
        }
    },
    methods: {
        drawChart() {
            console.log('drawChart()')
            if (!this.regressionData) return 

            const {X, y, X_new, y_pred} = this.regressionData
            const svg = d3.select(this.$refs.svg)
            const margin = {top:20, right:30, bottom:30, left:40}
            const width = this.svgWidth - margin.left - margin.right
            const height = this.svgHeight - margin.top - margin.bottom

            const xScale = d3.scaleLinear()
                            .domain(d3.extent(X))
                            .range([margin.left, width - margin.right]) // 해당 구간 안에 x좌표들 배치
            const yScale = d3.scaleLinear()
                            .domain([d3.min(y), d3.max(y)]) // extent하기엔 제곱식이라 너무 큼
                            .nice() // 보기좋게 표현해줘
                            .range([height - margin.bottom, margin.top])
            // 그래프 축 만들기
            svg.append("g") // x에 대해서
                    .attr("transform", `translate(0, ${height - margin.bottom})`)
                    .call(d3.axisBottom(xScale))
            
            svg.append("g") // y에 대해서
                    .attr("transform", `translate(${margin.left}, 0)`)
                    .call(d3.axisLeft(yScale))
            
            // 데이터 포인트 찍기
            svg.append("g")
                    .selectAll("circle")
                    .data(X)
                    .enter()
                    .append("circle")
                    .attr("cx", d => xScale(d))
                    .attr("cy", (d,i) => yScale(y[i]))
                    .attr("r", 3) // 반지름
                    .attr("fill", "blue") // 실선처리
            // line추적 (점들 잇기)
            const line = d3.line()
                    .x(d => xScale(d))
                    .y((d,i) => yScale(y_pred[i]))
            
            svg.append("path")
                    .datum(X_new)
                    .attr("fill","none")
                    .attr("stroke", "red")
                    .attr("stroke-width", 1.5)
                    .attr("d", line)
        }
    },
}

</script>