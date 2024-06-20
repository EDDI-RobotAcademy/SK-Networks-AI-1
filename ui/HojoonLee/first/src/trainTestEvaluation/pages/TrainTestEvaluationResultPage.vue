<template>
    <v-container class="chart-container">
        <h2>Train Test Evaluation</h2>
        <p>Accuracy: {{ accuracy }}</p>
        <svg ref="svg" :viewBox="`0 0 ${svgWidth} ${svgHeight}`"
                        preserveAspectRatio="xMidYMid meet"/>
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
import axiosInst from "@/utility/axiosInstance"

// 그래프 그리는 라이브러리 npm install d3 --legacy-peer-deps
import * as d3 from 'd3' 

export default {
    // 우리가 받아와야하는 local 정보들을 data에서 불러오기
    data () {
        return {
            accuracy:null,
            svgWidth: 600,
            svgHeight: 600,
            classificationReport: [],
            formattedReportData: []
        }
    },
    // 페이지가 생성되자마자(created) 실행하기 (mounted와 차이?)
    async created () {
        try {
            // fetch가 자체적으로 get과 동일함 
            // 현재는 d3와 fastapi, 딥러닝 hard skill(기능) 자체에 집중하기 때문에, 일단 soft skill(DDD)는 잠시 접어뒀음
            // 결론적으로 get으로 보내는 방식이 soft 방식(DDD), fetch로 보내는 방식은 좀 hard 방식
            const response = await fetch('http://localhost:33333/train-test-evaluation') // 얜 왜 get 요청 안보내지?
            const data = await response.json() // 이렇게 json형식으로 받아줘야 데이터가 들어옴 response.data 로 받으면 빈게 옴
            console.log('data:', data)

            this.accuracy = data.accuracy

            // 혼동행렬 그리기
            this.drawConfusionMatrix(data.confusion_matrix)
            // 분류결과 출력
            this.classificationReport = data.classification_report
            this.formatClassificationReport() // 분류결과 보여주는 함수
        } catch (error) {
            console.error('train test evaluation 데이터 확보 중 에러:', error)
        }
        window.addEventListener('resize', this.handleResize)
    },
    beforeUnmount () {
        window.removeEventListener('resize', this.handleResize)
    },
    methods: {
        drawConfusionMatrix(matrix) {
            // 혼동행렬 그리기
            const {svgWidth, svgHeight} = this
            const margin = {top:50, right:50, bottom:50, left:50}
            const width = svgWidth - margin.left - margin.right
            const height = svgHeight - margin.top - margin.bottom

            const svg = d3.select(this.$refs.svg)
                                .attr("width", width)
                                .attr("height", height)
            
            const maxValue = d3.max(matrix.flat())
            console.log('maxValue:', maxValue)
            
            //혼동행렬의 대각요소를 표현 (실제 클래스를 맞춘 경우들)
            const color = d3.scaleSequential()
                            .domain([0, maxValue])
                            .interpolator(d3.interpolateGreens)
            
            // 항상 3x3이 아닐 수 있으므로 계산해주기
            const cellSize = Math.min(width / matrix.length, height / matrix.length)
            
            // 사각형으로 cell 을 표현
            svg.append('g')
                    .attr('transform', `translate(${margin.left}, ${margin.top})`)
                    .selectAll("rect")
                    .data(matrix.flat()) // 고차원을 flatten 시키는 작업 => 행렬 데이터가 1개 씩 들어옴
                    .enter().append("rect")
                    .attr("x", (d, i) => (i % matrix.length) * cellSize)    // 같은 행을 표현할 때 같은 size를 가짐
                    .attr("y", (d, i) => Math.floor(i / matrix.length) * cellSize) // 같은 열을 표현 할 때 같은 size를 가짐
                    .attr("width", cellSize)
                    .attr("height", cellSize)
                    .style("fill", d => color(d))
                    .style("stroke", "#ccc")
                    .style("stroke-width", 1)

            // matrix.length 가 뭐지?
            console.log('matrix length:', matrix.length)

            // 행렬에 글자 추가하기
            svg.append('g')
                    .attr('transform', `translate(${margin.left}, ${margin.top})`)
                    .selectAll("text") // text 처리
                    .data(matrix.flat()) 
                    .enter().append("text")
                    .attr("x", (d, i) => (i % matrix.length) * cellSize + cellSize / 2) // cellSize/2 를 통해 셀의 가운데 오도록 처리
                    .attr("y", (d, i) => Math.floor(i / matrix.length) * cellSize + cellSize / 2)
                    .attr("dy", "0.65em")
                    .attr("text-anchor", "middle")
                    .text(d => d.toFixed(0)) // 소수점 몇 번째 까지 처리할거냐?
            
        },
        formatClassificationReport () {
            // fastapi에서 얻은 classifcationReport를 매핑해서 다음과 vue에서 써먹을 수 있게 dict data로 만들겠다.
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
        handleResize () {
            // 브라우저 크기 변경을 감지하면 0.2초 (200ms) 단위로 화면 크기 조정하여 다시 그림
            clearTimeout(this.resizeTimer)
            this.resizeTimer = setTimeout(() => {
                const chartContationer = this.$refs.chartContainer
                this.svgWidth = chartContationer.clientWidth
                this.svgHeight = chartContationer.clientHeight

                d3.select(this.$refs.svg)
                        .attr('viewBox', `0 0 ${this.svgWidth} ${this.svgHeight}`)

                this.createChart()
            }, 200)
        }
    }
}

</script>

<!-- scoped : 현재 페이지만 css 적용하겠다는 의미  -->
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