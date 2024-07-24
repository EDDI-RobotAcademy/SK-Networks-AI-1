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
import * as d3 from 'd3'
import axios from 'axios'
import axiosInstance from "@/utility/axiosInstance"

export default {
    name: 'ClusterVisualization',
    data() {
        return {
            centers: [],
            labels: [],
            points: []
        }
    },
    async mounted() {
        try {
            const response = await axiosInstance.fastapiAxiosInst.get('/kmeans-test')
            this.centers = response.data.centers
            this.labels = response.data.labels
            this.points = response.data.points
            this.createChart()
        } catch (error) {
            console.error("Error fetching data: ", error)
        }
    },
    methods: {
        createChart() {
            const svg = d3.select(this.$refs.chart)
                .append('svg')
                .attr('width', '100%')
                .attr('height', '500px')
                .attr('viewBox', '0 0 800 500')
                .append('g')
                .attr('transform', 'translate(50,50)')

            const width = 700
            const height = 400

            const xScale = d3.scaleLinear()
                .domain(d3.extent(this.points, d => d[0]))
                .range([0, width])

            const yScale = d3.scaleLinear()
                .domain(d3.extent(this.points, d => d[1]))
                .range([height, 0])

            const color = d3.scaleOrdinal(d3.schemeCategory10)

            // Draw points
            svg.selectAll('circle')
                .data(this.points)
                .enter()
                .append('circle')
                .attr('cx', d => xScale(d[0]))
                .attr('cy', d => yScale(d[1]))
                .attr('r', 5)
                .attr('fill', (d, i) => color(this.labels[i]))

            // Draw centers
            svg.selectAll('rect')
                .data(this.centers)
                .enter()
                .append('rect')
                .attr('x', d => xScale(d[0]) - 10)
                .attr('y', d => yScale(d[1]) - 10)
                .attr('width', 20)
                .attr('height', 20)
                .attr('fill', 'purple')
        }
    }

}
</script>