<template>
    <v-container>
        <svg ref="svg" :viewBox="`0 0 ${svgWidth} ${svgHeight}`"
                        preserveAspectRatio="xMidYMid meet"></svg>
    </v-container>
</template>

<script>
import * as d3 from 'd3'

export default {
    data () {
        return {
            svgWidth: 500,
            svgHeight: 350,
            regressionData: null,
        }
    },
    async created () {
        try {
            const response = 
                await fetch('http://192.168.0.42:33333/polynomial-regression')
            const data = await response.json()
            this.regressionData = data
            console.log('data:', data)
            this.drawChart()
        } catch (error) {
            console.error('다항 회귀 데이터 확보 중 에러:', error)
        }
    },
    methods: {
        drawChart () {
            console.log('drawChart()')

            if (!this.regressionData) return

            const { X, y, X_new, y_pred } = this.regressionData
            const svg = d3.select(this.$refs.svg)
            const margin = { top: 20, right: 30, bottom: 30, left: 40 }
            const width = this.svgWidth - margin.left - margin.right
            const height = this.svgHeight - margin.top - margin.bottom

            const xScale = d3.scaleLinear()
                                .domain(d3.extent(X))
                                .range([margin.left, width - margin.right])

            const yScale = d3.scaleLinear()
                                .domain([d3.min(y), d3.max(y)])
                                .nice()
                                .range([height - margin.bottom, margin.top])

            svg.append("g")
                    .attr("transform", `translate(0, ${height - margin.bottom})`)
                    .call(d3.axisBottom(xScale))

            svg.append("g")
                    .attr("transform", `translate(${margin.left}, 0)`)
                    .call(d3.axisLeft(yScale))

            svg.append("g")
                    .selectAll("circle")
                    .data(X)
                    .enter()
                    .append("circle")
                    .attr("cx", d => xScale(d))
                    .attr("cy", (d, i) => yScale(y[i]))
                    .attr("r", 3)
                    .attr("fill", "blue")

            const line = d3.line()
                    .x(d => xScale(d))
                    .y((d, i) => yScale(y_pred[i]))

            svg.append("path")
                    .datum(X_new)
                    .attr("fill", "none")
                    .attr("stroke", "red")
                    .attr("stroke-width", 1.5)
                    .attr("d", line)
        }
    }
}
</script>