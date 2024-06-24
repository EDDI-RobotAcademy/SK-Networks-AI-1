<template>
    <v-container class="chart-container">
        <h2>Logistic Regression Chart</h2>
        <p>Accuracy: {{ accuracy }} </p>
        <div ref="chartContainer" class="chart-wrapper">
            <svg ref="svg" :viewBox="`0 0 ${svgWidth} ${svgHeight}`"
                            preserveAspectRatio="xMidYMid meet"/>
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
            accuracy : 0,
            X: [],
            y: [],
            x_values: [],
            y_values: [],
            svgWidth: 0,
            svgHeight: 0,
            margin: { top:20, right:50, bottom:50, left:50 },
            resizeTimer: null,
        }
    },
    // mounted 에서 fetch된 data들을 불러오기
    mounted () {
        this.fetchLogisticRegressionData()
        window.addEventListener('resize', this.handleResize)
    },
    beforeUnmount () {
        window.removeEventListener('resize', this.handleResize)
    },
    methods: {
        async fetchLogisticRegressionData () {
            // 이제 요청을 장고가 아닌 fastapi에 보내므로 djangoaxiosinst를 쓰지 않음 >> 관련 정보들 .env에 추가하기
            // fastapi의 logistic-regression 이란 곳에 get요청 보냄
            try {
                const response = await axiosInst.fastapiAxiosInst.get('/logistic-regression')
                const data = response.data
                console.log('result: ', data)
                
                this.accuracy = data.accuracy
                this.X = data.data_point.X
                this.y = data.data_point.y
                this.x_values = data.decision_boundary.x_values
                this.y_values = data.decision_boundary.y_values
                this.createChart()
            } catch (error) {
                console.error('로지스틱 회귀 분석 중 에러 발생:', error)
            }
        },
        createChart() {
            if (!this.X.length || !this.y.length ||
            !this.x_values.length || !this.y_values.length) {
                console.warn('데이터가 제대로 처리되지 않고 있습니다.')
                return
            }
            // svg 컨테이너 크기 설정
            const chartContainer = this.$refs.chartContainer
            this.svgWidth = chartContainer.clientWidth
            this.svgHeight = chartContainer.clientHeight
            
            // d3 플로팅 목적으로 사용할 위의 template에 있는 ref svg 요소를 초기화
            d3.select(this.$refs.svg).selectAll("*").remove() // refs란 곳에 그릴거야 
            
            // svg 요소 크기 지정
            const svg = d3.select(this.$refs.svg)
                        .attr('width', this.svgWidth)
                        .attr('height', this.svgHeight)
            // 마진 설정 및 그룹 요소 추가 >> 쉽게 얘기해서 그래프가 너무 바짝 붙어있으면 모양이 안예뻐서 주변으로 여백을 생성
            const g = svg.append('g')
                    .attr('transform',
                    `translate(${this.margin.left}, ${this.margin.top})`)

            // numpy 작업시 [:, 0], [:, 1]에 해당하는 x 성분, y 성분을 추출함
            // 각각의 최소, 최대값을 domain으로 설정하고 실제 차트 크기에 맞춰서 범위를 지정하도록 range()로 지정하도록
            // 예로 50 ~ 150 사이 범주 데이터가 있으면, 강제로 0 ~ 100으로 스케일
            const x = d3.scaleLinear()
                    .domain(d3.extent(this.X, d => d[0]))
                    .range([0, this.svgWidth - this.margin.left - this.margin.right])
            
            const y = d3.scaleLinear()
                    .domain(d3.extent(this.y, d => d[1]))
                    .range([this.svgHeight - this.margin.top - this.margin.bottom, 0])
            // x축을 하단에 배치, translate는 평행이동을 의미함, x 방향으로 0, y 방향으로 아래 계산 수치만큼 평행이동
            // 결론적으로 외관상 이쁘게 하려고 attr을 사용하여 translate 시킨 것임
            g.append('g')
                    .attr('transform',
                    `translate(0, ${this.svgHeight - this.margin.top - this.margin.bottom})`)
                    .call(d3.axisBottom(x))
            
            // y축은 좌측에 설정
            g.append('g')
                .call(d3.axisLeft(y))
            
            // 그래프에 data point 찍기,
            // 실제 데이터에 해당하는 정보를 'circle'로 표현합니다. (아직 붙인건 아님)
            g.selectAll('circle')
                .data(this.X) // 그림 그릴 데이터인 X (x,y) 벡터를 배치합니다.
                .enter() // enter를 통해 실제 웹 브라우저 상에서 관리할 수 있는 데이터로 구성함 (반드시 필요한 과정)
                .append('circle') // 실제 데이터에 해당하는 영역 좌표에 'circle'을 붙입니다.
                .attr('cx', d => x(d[0])) // circle을 붙일건데 속성값을 어떻게 할 것이냐를 .attr을 통해서 x,y 좌표 지정
                .attr('cy', d => x(d[1]))
                .attr('r', 5) // r : 원의 반지름 설정
                .style('fill', (d, i) => this.y[i] === 1 ? 'green' : 'blue') // 실제 X에 대응하는 y값이 1인 경우 초록색,
                                                                             // 아닌 경우 파랑색으로 그립니다.
            // 결정 경계를 파악하기 위한 선 그릴 준비
            const line = d3.line()
                        .x(d => x(d[0]))
                        .y(d => x(d[1]))
            // decision boundary
            // 실제 fastapi에서 분석했던 로지스틱 회귀 분석의 결정경계 x 값을 추출함
            // x_values는 100개의 데이터이므로 아래 map을 통해서 낱개인 x_value로 재해석됨
            // 즉 x_value인 낱개 데이터와 인덱스 번호(i)로 구성되고
            // 이 정보들을 전부 [x_value, this.y_values[i]]로 매핑하여 좌표화 함
            const decisionboundary = this.x_values.map((x_values, i) => [x_values, this.y_values[i]])

            g.append('path')
                .datum(decisionboundary)
                .attr('d', line)
                .attr('stroke', 'red')
                .attr('stroke-width', 2)
                .attr('fill', 'none')
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
.chart-container {
    width: 80%;
    height: 60%;
    margin: auto;
}

.chart-wrapper {
    position: relative;
    width: 100%;
    height: 100%;
}
</style>