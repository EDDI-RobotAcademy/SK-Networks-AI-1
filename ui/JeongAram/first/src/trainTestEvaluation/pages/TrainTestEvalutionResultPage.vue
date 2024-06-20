<template>
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
                        <th>F1-Score</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="report in formattedReportData" :key="report.metric">
                        <td>{{  report.metric }}</td>
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

import axiosInst from "@/utility/axiosInstance"
// npm install d3 --legacy-peer-deps
import * as d3 from 'd3'


export default {
    // 우리가 받아와야하는 local 정보들을 data에서 불러오기
    data() {
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
            // 현재 d3와 fastapi, 딥러닝 hard skill(기능) 자체에 집중하기 때문에
            // 일단 soft skill(DDD)는 잠시 접어뒀음
            const response = await fetch('http://localhost:33333/train-test-evaluation')
            const data = await response.json()  // json 형식으로 데이터를 받아와야함 아니면 빈 게 옴
            console.log('data:', data)

            this.accuracy = data.accuracy  // ??this. 는 위에 data()에서 선언했던 것들을 가리킴 (self느낌)

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
            // console.log('컨.퓨.전 매트릭스')
            const { svgWidth, svgHeight } = this
            const margin = { top: 50, right: 50, bottom: 50, left: 50 }
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
                    .style("stroke", "#ccc")  // 눈금 그어줌
                    .style("stroke-width", 1)

            svg.append('g')
                    .attr('transform', `translate(${margin.left}, ${margin.top})`)
                    .selectAll("text")
                    .data(matrix.flat())
                    .enter().append("text")
                    .attr("x", (d, i) => (i % matrix.length) * cellSize + cellSize / 2) 
                    .attr("y", (d, i) => Math.floor(i / matrix.length) * cellSize + cellSize / 2)
                    .attr("dy", "0.65em")
                    .attr("text-anchor", "middle")
                    .text(d => d.toFixed())  // toFixed() 소수점 자리

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

<!-- scoped: 현재 페이지만 css 적용하겠다-->
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
    background-color: #f2f2f2;
}

</style>