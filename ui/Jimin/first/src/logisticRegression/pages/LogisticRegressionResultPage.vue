<template>
    <v-container class="chart-contatiner">
        <h2>Logistic Regression Chart</h2>
        <p>Accuracy: {{ accuracy }}</p>
        <div ref="chartContainer" class="chart-wrapper">
            <svg ref="svg" :viewBox="`0 0 ${svgWidth} ${svgHeight}`"
                            preserveAspectRatio="xMidYMid meet">
            </svg>
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
            accuracy: 0,
            x: [],
            y: [],
            x_values: [],
            y_values: [],
            svgWidth: 0,
            svgHeight: 0,
            margin: {top: 20, right:50, bottom: 50, left: 50 },
            resizeTimer: null,
        }
    },
    mounted () {
        this.fetchLogisticRegressionData()
        window.addEventListener('resize', this.handleResize)

    },
    beforeUnmount () {
        window.removeEventListener('resize', this.handleResize)
    },
    methods: {
        async fetchLogisticRegressionData () {
            try {
                const response = await axiosInst.fastapiAxiosInst.get('/logistic-regression') 
                

                const data = response.data
                console.log('result:', response.data)

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
        createChart () {

            // svg 컨테이너 크기 설정
            if (!this.X.length || !this.y.length || !this.x_values.length || !this.y_values.length) {
                console.warn('데이터가 제대로 처리되지 않고 있습니다!')
                return
            }

            const chartContainer = this.$refs.chartContainer
            this.svgWidth = chartContainer.clientWidth
            this.svgHeight = chartContainer.clientHeight

            // d3 플롯팅 목적으로 사용할 template에 있는 ref svg 요소를 초기화
            d3.select(this.$refs.svg).selectAll("*").remove()

            // svg 요소 크기 지정
            const svg = d3.select(this.$refs.svg).attr('width', this.svgWidth).attr('height', this.svgHeight)
            
            // 마진 설정 및 그룹 요소 추가
            // 쉽게 얘기해서 그래프가 너무 바짝 붙어 있으면 모양이 안 예뻐서
            // 주변으로 여백을 일부 생성하도록 하는 부분임
            const g = svg.append('g').attr('transform', `translate(${this.margin.left}, ${this.margin.top})`)

            // numpy 작업시 [:, 0], [:, 1]에 해당하는 x 성분, y 성분을 추출함
            // 각각의 최소, 최대값을 domain으로 설정하고
            // 실제 차트 크기에 맞춰서 범위를 지정하도록 range()로 지정
            // 예로 50~150 사이 범주 데이터가 있다면
            // 강제로 0~100으로 스케일
            // 좀 더 독특한 예라면
            // -1000~+1000을 -100~+100으로 스케일
            const x = d3.scaleLinear().domain(d3.extent(this.X, d => d[0])).range([0, this.svgWidth - this.margin.left - this.margin.right])
            
            const y = d3.scaleLinear().domain(d3.extent(this.y, d => d[1])).range([this.svgHeight - this.margin.top - this.margin.bottom, 0])

            // x 축 설정, 하단에 배치
            // translate는 평행 이동을 의미함
            // x 방향으로 0, y 방향으로 아래 계산 수치만큼 평행이동
            // 결론적으로 외관적으로 보기 좋게 만들려고
            // attr을 사용하여 translae 시킨것
            g.append('g').attr('transform', `translate(0, ${this.svgHeight - this.margin.top - this.margin.bottom})`)
                            .call(d3.axisBottom(x)) // x축 잡아주는 코드

            // y 축 좌측에 배치
            g.append('g').call(d3.axisLeft(y))

            // 실제 데이터에 해당하는 정보를 '원'으로 표현
            // 그림 그릴 데이터인 X (x,y) 벡터를 배치합니다.
            // enter()를 통해서 실제 웹 브라우저 상에서 관리할 수 있는 데이터를 구성함
            // append('circle')은 실제 데이터에 해당하는 영역 좌표에 '원'을 붙입니다.
            // 붙이는데 속성 값을 어떻게 할 것인가가
            // attr('cx', d => x(d[0]))입니다.
            // 원의 x좌표와 아래 attr('cy', d => x(d[1]))를 통해 y 좌표 지정
            // attr('r', 5)의 경우 원의 반지름 설정
            // 실제 x에 대응하는 y 값이 있습니다.
            // 이 y값이 1인 경우 초록색, 0인 경우 파랑색으로 그립니다.
            g.selectAll('circle')
                .data(this.X)
                .enter()
                .append('circle')
                .attr('cx', d => x(d[0]))
                .attr('cy', d => x(d[1]))
                .attr('r', 5)
                .style('fill', (d, i) => this.y[i] === 1 ? 'green' : 'blue')

            // 결정 경계 (Decision Boundary)를 파악하기 위한 선 그릴 준비
            const line = d3.line()
                    .x(d => x(d[0]))
                    .y(d => x(d[1]))
            // 실제 fastapi에서 분석했던 로지스틱 회귀 분석의 결정 경계 x 값을 추출함
            // x_values는 100개의 데이터이므로 아래 map을 통해서 낱개인 x_value로 재해석됨
            // 즉 x_vlaue인 낱개 데이터와 인덱스 번호(i)로 구성되고
            // 이 정보들을 전부 [x_value, this.y_values[i]로 맵핑하여 좌표화함]
            const decisionBoundary = this.x_values.map((x_value, i) => [x_value, this.y_values[i]])
        
            // 여기서 실제 결정 경계에 해당하는 라인을 빨간색 선으로 그립니다.
            // stroke <- red는 선 색상 빨강
            // stroke-width <- 선 굵기
            // fill none <- 실선
            g.append('path').datum(decisionBoundary)
                            .attr('d', line)
                            .attr('stroke', 'red')
                            .attr('stroke-width', 2)
                            .attr('fill', 'none')
        },
        handleResize () {
            clearTimeout(this.resizeTimer)
            this.resizeTimer = setTimeout(() => {
                const chartContainer = this.$refs.chartContainer
                this.svgWidth = chartContainer.clientWidth
                this.svgHeight = chartContainer.clientHeight

                d3.select(this.$refs.svg).attr('viewBox', `0 0 ${this.svgWidth} ${this.svgHeight}`)

                this.createChart()
            }, 200)
        }
    }
}
</script>
<!-- scoped 사용하면 이 페이지에만 style 적용 -->
<style scoped>
.chart-container {
    width: 80%;
    height: 80%;
    margin: auto;
}

.chart-wrapper {
    position: relative;
    width: 100%;
    height: 100%;
}
</style>