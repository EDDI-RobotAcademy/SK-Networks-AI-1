<template>
    <v-card>
        <v-card-title className="headline">Confusion Matrix</v-card-title>
        <v-card-text>
            <svg ref="confusionMatrix"/>
        </v-card-text>
    </v-card>
</template>

<script>
import * as d3 from 'd3'

export default {
    props: {
        confusionMatrix: Array,
    },
    mounted () {
        this.drawConfusionMatrix()
    },
    methods: {
        drawConfusionMatrix () {
            const { confusionMatrix } = this
            const svg = d3.select(this.$refs.confusionMatrix)

            const margin = { top: 50, right: 50, bottom: 50, left: 50 }
            const width = 500 - margin.left - margin.right
            const height = 500 - margin.top - margin.bottom

            svg.attr('width', width + margin.left + margin.right)
                .attr('height', height + margin.top + margin.bottom)

            const matrix = svg.append('g')
                .attr('transform', `translate(${margin.left}, ${margin.top})`)

            const colorScale = d3.scaleSequential(d3.interpolateReds)
                .domain([0, d3.max(confusionMatrix, d => d3.max(d))])

            const cellSize = Math.min(width / confusionMatrix.length,
                                    height / confusionMatrix.length)

            const cells = matrix.selectAll('.cell')
                .data(confusionMatrix)
                .enter().append('g')
                .attr('class', 'cell')
                .attr('transform', (d, i) => `translate(0, ${i * cellSize})`)

            cells.selectAll('.rect')
                .data(d => d)
                .enter().append('rect')
                .attr('width', cellSize)
                .attr('height', cellSize)
                .attr('x', (d, i) => i * cellSize)
                .attr('fill', d => colorScale(d))
                .append('title')
                .text(d => d)

            cells.selectAll('.cell-text')
                .data(d => d)
                .enter().append('text')
                .attr('class', 'cell-text')
                .attr('x', (d, i) => i * cellSize + cellSize / 2)
                .attr('y', cellSize/2)
                .attr('dy', '.35em')
                .attr('text-anchor', 'middle')
                .text(d => d)
        }
    }
}

</script>