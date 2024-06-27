<template>
    <v-container>
        <v-row>
            <v-col>
                <h1>k-means Clustering Visualization</h1>
                <div ref="chart" :style="{ width: '100%', height: '500px' }"></div>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import * as d3 from 'd3';
import axios from 'axios';

export default {
    name: 'ClusterVisualization',
    data() {
        return {
            centers: [],
            labels: [],
            points: []
        };
    },
    async mounted() {
        try {
            const response = await axios.get('http://localhost:33333/kmeans-test');
            this.centers = response.data.centers;
            this.labels = response.data.labels;
            this.points = response.data.points;
            this.createChart();
        } catch (error) {
            console.error("Error fetching data: ", error);
        }
    },
    methods: {
        createChart() {
            // svg 요소 생성 및 설정
            // svg 요소 폭 100%, 높이는 500px
            // 내부에 배치하는 View Box를 svg 요소에 맞게 스케일
            // 그리고 여백을 생성함
            const svg = d3.select(this.$refs.chart)
                .append('svg')
                .attr('width', '100%')
                .attr('height', '500px')
                .attr('viewBox', '0 0 800 500')
                .append('g')
                .attr('transform', 'translate(50,50)');

            const width = 700;
            const height = 400;

            // x, y 데이터에 따른 스케일링
            const xScale = d3.scaleLinear()
                .domain(d3.extent(this.points, d => d[0]))
                .range([0, width]);

            const yScale = d3.scaleLinear()
                .domain(d3.extent(this.points, d => d[1]))
                .range([height, 0]);

            // 10개의 범주형 색상 스케일링
            // 데이터 포인트의 클러스터 라벨에 따라 색상이 자동 지정
            const color = d3.scaleOrdinal(d3.schemeCategory10);

            // Draw points
            // 기존의 circle을 포함하여 모든 circle 요소를 선택함(초반에는 선택될 것 없음)
            // data를 통해 실제 포인트를 찍어야 하는 정보를 맵핑
            // append('circle')을 통해 각 데이터에 대해 실제 'circle' 요소를 추가함
            // .attr('cx') .attr('cy') 를 통해 x, y 좌표를 설정함
            // .attr('r') 으로 반지름 값 설정
            // .attr('fill' (d, i) => color(this.labels[i])) 를 통해
            // 데이터 포인트의 색상을 클러스터 라벨에 따라 변경
            svg.selectAll('circle')
                .data(this.points)
                .enter()
                .append('circle')
                .attr('cx', d => xScale(d[0]))
                .attr('cy', d => yScale(d[1]))
                .attr('r', 5)
                .attr('fill', (d, i) => color(this.labels[i]));

            // Draw centers
            // 마찬가지로 rect라는 모든 요소 선택(초반엔 아무것도 없음)
            // this.centers로 실제 중앙값을 맵핑함
            // 사각형의 크기는 20, 20으로 잡고 보라색으로 구성
            svg.selectAll('rect')
                .data(this.centers)
                .enter()
                .append('rect')
                .attr('x', d => xScale(d[0]) - 10)
                .attr('y', d => yScale(d[1]) - 10)
                .attr('width', 20)
                .attr('height', 20)
                .attr('fill', 'purple');
        }
    }
};
</script>

<style scoped>
</style>
