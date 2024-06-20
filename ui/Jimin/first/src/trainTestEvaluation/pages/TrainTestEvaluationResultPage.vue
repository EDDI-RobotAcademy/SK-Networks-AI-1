<template>
    <v-container class="chart-contatiner">
        <h2>Train Test Evaluation</h2>
        <p>Accuracy: {{ accuracy }}</p>
        <svg ref="svg" :viewBox="`0 0 ${svgWidth} ${svgHeight}`"
                        preserveAspectRatio="xMidYMid meet"></svg>
        <div class="report">
            <h2>Classificaion Report</h2>
            <table class="classification-report-table">
                <thead>
                    <tr>
                        <th>Metric</th>
                        <th>Precision(정밀도)</th>
                        <th>Recall(재현율)</th>
                        <th>F1-Score</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="report in formattedReportData" :key="report.metric">
                        <td>{{ report.metric }}</td>
                        <td>{{ report.precision }}</td>
                        <td>{{ report.recall }}</td>
                        <td>{{ report[`f1-score`] }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        
    </v-container>
</template>

<script>
import axiosInst from '@/utility/axiosInstance'
import * as d3 from 'd3'
// npm install d3 --legacy-peer-deps

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
        try{
            // fetch가 자체적으로 get과 동일함
            // 현재 d3와 딥러닝 hard skill(기능) 자체에 집중하기 때문에
            // 일단 soft skill(DDD)는 잠시 접어뒀음
            const response = await fetch('http://localhost:33333/train-test-evaluation')
            const data = await response.json()
            console.log('data:', data)

            this.accuracy = data.accuracy

            this.drawConfusionMatrix(data.confusion_matrix)

            this.classificationReport = data.classification_report
            this.formatClassificationReport()
        } catch (error) {
            console.error('train test evaluation 데이터 확보 중 에러:', error)
        }
        window.addEventListener('resize', this.handleResize)

    },
    beforeUnmount () {
        window.removeEventListener('resize', this.handleResize)
    },
    methods: {
        drawConfusionMatrix (matrix) {
            const { svgWidth, svgHeight } = this
            const margin = {top: 50, right: 50, bottom: 50, left: 50}
            const width = svgWidth - margin.left - margin.right
            const height = svgHeight - margin.top - margin.bottom

            const svg = d3.select(this.$refs.svg)
                            .attr("width", width)
                            .attr("height", height)

            const maxValue = d3.max(matrix.flat())
            console.log('maxValue:', maxValue)

            const color = d3.scaleSequential()
                            .domain([0, maxValue])
                            .interpolator(d3.interpolateGreens)

            const cellSize = Math.min(width / matrix.length, height / matrix.length)
            console.log('cellSize:', cellSize)
            console.log('matrix length:', matrix.length)

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
                    .style("stroke", "#ccc") // 눈금 그어줌
                    .style("stroke-width", 1)

            svg.append('g')
                    .attr('transform', `translate(${margin.left} ${margin.top})`)
                    .selectAll("text")
                    .data(matrix.flat())
                    .enter().append("text")
                    .attr("x", (d, i) => (i % matrix.length) * cellSize + cellSize / 2)
                    .attr("y", (d, i) => Math.floor(i / matrix.length) * cellSize + cellSize / 2)
                    .attr("dy", "0.65em")
                    .attr("text-anchor", "middle")
                    .text(d => d.toFixed(2)) // 소숫점 몇번째까지 표현 할꺼야
                    
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
        
        
    }
}
</script>
<!-- scoped 사용하면 이 페이지에만 style 적용 -->
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