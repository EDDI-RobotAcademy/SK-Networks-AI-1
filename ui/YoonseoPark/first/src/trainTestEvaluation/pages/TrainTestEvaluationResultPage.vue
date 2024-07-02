<template lang="">
    <v-container class="chart-container">
        <h2>Train Test Evaluation</h2>
        <p>Accuracy: {{  accuracy }}</p>
        <svg ref="svg" :viewBox="`0 0 ${svgWidth} ${svgHeight}`"
                        preserveAspectRatio="xMidYMid meet"></svg>
        <div class="report">
            <h2>Classification Report</h2>
            <table class="classification-report-table">
                <thead>
                    <tr>
                        <th>Metric</th>
                        <th>Precision(정밀도)</th>
                        <th>Recall(재현율)</th>
                        <th>f1-Score</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="report in formattedReportData" :key="report.metric">
                        <td>{{  report.metric }}</td>
                        <td>{{  report.precision }}</td>
                        <td>{{  report.recall }}</td>
                        <td>{{  report['f1-score'] }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </v-container>
</template>

<script>
import axiosInstance from '@/utility/axiosInstance'
import * as d3 from 'd3'

export default {
    data () {
        return {
            accuracy: null,
            svgWidth: 600,
            svgHeight: 600,
            classificationReport: [],
            formattedReportData: [],
        }
    },
    async created () {
        try {
            // fetch가 자체적으로 get과 동일함
            // 현재 d3와 딥러닝 hard skill(기능) 자체에 집중하기 때문에
            // 일단 soft skill(DDD)는 잠시 접어뒀음
            const response = await axiosInstance.fastapiAxiosInst.get('/train-test-evaluation')
            const data = response.data
            // const response = await fetch('http://localhost:33333/train-test-evaluation')
            // const data = await response.json()
            console.log('data:', data)

            this.accuracy = data.accuracy

            this.drawConfusionMatrix(data.confusion_matrix)

            this.classificationReport = data.classification_report
            this.formatClassificationReport()
        } catch (error) {
            console.error('train test evaluation 데이터 확보 중 에러:', error)
        }
    },
    methods: {
        drawConfusionMatrix (matrix) {
            const { svgWidth, svgHeight } = this
            const margin = { top: 50, right: 50, bottom: 50, left: 50 }
            const width = svgWidth - margin.left - margin.right
            const height = svgHeight - margin.top - margin.bottom

            const svg = d3.select(this.$refs.svg)
                            .attr('width', width)
                            .attr('height', height)

            const maxValue = d3.max(matrix.flat())
            console.log('maxValue:', maxValue)

            const color = d3.scaleSequential()
                            .domain([0, maxValue])
                            .interpolator(d3.interpolateGreens)

            const cellSize = Math.min(width / matrix.length, height / matrix.length)

            svg.append('g')
                    .attr('transform', `translate(${margin.left}, ${margin.top})`)
                    .selectAll("rect")
                    .data(matrix.flat())
                    .enter().append("rect")
                    .attr("x", (d, i) => (i % matrix.length) * cellSize)
                    .attr("y", (d, i) => Math.floor(i / matrix.length) * cellSize)
                    .attr("width", cellSize)
                    .attr("height", cellSize)
                    .style("fill", d => color(d))
                    .style("stroke", "#ccc")
                    .style("stroke-width", 3)

            svg.append('g')
                    .attr('transform', `translate(${margin.left}, ${margin.top})`)
                    .selectAll("text")
                    .data(matrix.flat())
                    .enter().append("text")
                    .attr("x", (d, i) => (i % matrix.length) * cellSize + cellSize / 2)
                    .attr("y", (d, i) => Math.floor(i / matrix.length) * cellSize + cellSize / 2)
                    .attr("dy", "0.65em")
                    .attr("text-anchor", "middle")
                    .text(d => d.toFixed(0))
        },
        formatClassificationReport () {
            const formattedData = this.classificationReport.map((report, index) => {
                const formattedReport = {
                    metric: report.metric,
                    precision: report.precision.toFixed(2),
                    recall: report.recall.toFixed(2),
                    'f1-score': report['f1-score'].toFixed(2),
                }
                
                return formattedReport
            })

            this.formattedReportData = formattedData
        },
        createChart () {
            if (!this.X.length || !this.y.length || 
                !this.x_values.length || !this.y_values.length) {
                console.warn('데이터가 제대로 처리되지 않고 있습니다!')
                return
            }
            // svg 컨테이너 크기 설정
            const chartContainer = this.$refs.chartContainer
            this.svgWidth = chartContainer.clientWidth
            this.svgHeight = chartContainer.clientHeight
            // d3 플롯팅 목적으로 사용할 template에 있는 ref svg 요소를 초기화
            d3.select(this.$refs.svg).selectAll("*").remove()
            
            // svg 요소 크기 지정
            const svg = d3.select(this.$refs.svg)
                            .attr('width', this.svgWidth)
                            .attr('height', this.svgHeight)

            const g = svg.append('g')
                        .attr('transform', 
                            `translate(${this.margin.left}, ${this.margin.top})`)

            const x = d3.scaleLinear()
                        .domain(d3.extent(this.X, d => d[0]))
                        .range([0, this.svgWidth - this.margin.left - this.margin.right])
            const y = d3.scaleLinear()
                        .domain(d3.extent(this.y, d => d[1]))
                        .range([this.svgHeight - this.margin.top - this.margin.bottom, 0])

            g.append('g')
                .attr('transform', 
                    `translate(0, ${this.svgHeight - this.margin.top - this.margin.bottom })`)
                .call(d3.axisBottom(x))
            // y 축은 좌측에 배치
            g.append('g')
                .call(d3.axisLeft(y))

            g.selectAll('circle')
                .data(this.X)
                .enter()
                .append('circle')
                .attr('cx', d => x(d[0]))
                .attr('cy', d => x(d[1]))
                .attr('r', 5)
                .style('fill', (d, i) => this.y[i] === 1 ? 'green' : 'blue')

            const line = d3.line()
                    .x(d => x(d[0]))
                    .y(d => x(d[1]))

            const decisionBoundary = this.x_values.map((x_value, i) => [x_value, this.y_values[i]])
            console.log('decisionBoundary:', decisionBoundary)

            g.append('path')
                .datum(decisionBoundary)
                .attr('d', line)
                .attr('stroke', 'red')
                .attr('stroke-width', 2)
                .attr('fill', 'none')
        },
        handleResize () {
            // 브라우저 크기 변경을 감지하면 0.2초 단위로 화면 크기 조정하여 다시 그림
            clearTimeout(this.resizeTimer)
            this.resizeTimer = setTimeout(() => {
                const chartContainer = this.$refs.chartContainer
                this.svgWidth = chartContainer.clientWidth
                this.svgHeight = chartContainer.clientHeight

                d3.select(this.$refs.svg)
                        .attr('viewBox', `0 0 ${this.svgWidth} ${this.svgHeight}`)

                this.createChart()
            }, 200)
        }
    }
}
</script>

<style scoped>
.report {
    margin-top: 20px;
    text-align: center;
}

.classification-report-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

.classification-report-table th,
.classification-report-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
}

.classification-report-table th {
    background-color: #f2f2f2
}
</style>