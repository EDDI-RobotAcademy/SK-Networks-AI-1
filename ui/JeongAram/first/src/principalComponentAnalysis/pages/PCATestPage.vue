<template>
    <v-container>
        <v-row>
            <v-col>
                <v-btn @click="fetchPCAData">PCA Analysis</v-btn>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <div ref="originalChart"/>
            </v-col>
            <v-col>
                <div ref="pcaChart"/>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axiosInstance from '@/utility/axiosInstance';
import axios from 'axios';
import * as d3 from 'd3'

export default {
    data () {
        return {
            pcaData: null,
            originalData: null,
            explainedVarianceRatio: null,
        }
    },
    methods: {
        async fetchPCAData () {
            const response = await axiosInstance.fastapiAxiosInst.get('http://192.168.0.46:33333/pca-analysis')
            console.log('response:', response)

            const data = await response.data

            this.originalData = data.original_data
            this.pcaData = data.pca_data
            this.explainedVarianceRatio = data.explained_variance_ratio

            this.createChart ()
        },
        createChart () {
            if (!this.pcaData || !this.originalData) return

            this.createOriginalChart()
            this.createPCAChart()
        },
        createOriginalChart () {
            console.log('createOriginalChart()')

            const svg = d3.select(this.$refs.originalChart).append('svg')
                            .attr('width', 400)
                            .attr('height', 400)
            
            const margin = { top: 20, right: 30, bottom: 40, left: 40 }
            const width = svg.attr("width") - margin.left - margin.right
            const height = svg.attr("height") - margin.top - margin.bottom
            
            const g = svg.append("g").attr("transform", `translate(${margin.left}, ${margin.top})`)
            const x = d3.scaleLinear()
                    .domain(d3.extent(this.originalData, d => d[0]))
                    .range([0, width])

            const y = d3.scaleLinear()
                    .domain(d3.extent(this.originalData, d => d[1]))
                    .range([height, 0])

            g.append("g") // x축 생성
                    .attr("transform", `translate(0, ${height})`)
                    .call(d3.axisBottom(x))
            
            g.append("g").call(d3.axisLeft(y))

            g.selectAll(".dot")
                    .data(this.originalData)
                    .enter().append("circle")
                    .attr("class", ".dot")
                    .attr("cx", d => x(d[0]))
                    .attr("cy", d => y(d[1]))
                    .attr("r", 3.5)
                    .style("fill", "steelblue")

            svg.append("text")
                    .attr("x", (width / 2))
                    .attr("y", margin.top)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "16px")
                    .style("text-decoration", "underline")
                    .text("Original Data")
        },
        createPCAChart () {
            console.log('createPCAChart()')

            console.log('createPCAChart()')

            const svg = d3.select(this.$refs.pcaChart).append('svg')
                            .attr('width', 400)
                            .attr('height', 400)
            
            const margin = { top: 20, right: 30, bottom: 40, left: 40 }
            const width = svg.attr("width") - margin.left - margin.right
            const height = svg.attr("height") - margin.top - margin.bottom
            const g = svg.append("g").attr("transform", `translate(${margin.left}, ${margin.top})`)
            const x = d3.scaleLinear()
                    .domain(d3.extent(this.pcaData, d => d[0]))
                    .range([0, width])

            const y = d3.scaleLinear()
                    .domain(d3.extent(this.pcaData, d => d[1]))
                    .range([height, 0])

            g.append("g") // x축 생성
                    .attr("transform", `translate(0, ${height})`)
                    .call(d3.axisBottom(x))
            
            g.append("g").call(d3.axisLeft(y))

            g.selectAll(".dot")
                    .data(this.pcaData)
                    .enter().append("circle")
                    .attr("class", "dot")
                    .attr("cx", d => x(d[0]))
                    .attr("cy", d => y(d[1]))
                    .attr("r", 3.5)
                    .style("fill", "orange")

            svg.append("text")
                    .attr("x", (width / 2))
                    .attr("y", margin.top)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "16px")
                    .style("text-decoration", "underline")
                    .text(`PCA Data: PC1=${(this.explainedVarianceRatio[0] * 100).toFixed(2)}%, PC2=${(this.explainedVarianceRatio[1] * 100).toFixed(2)}%`)
        }
    },
}
</script>