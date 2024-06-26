<template>
  <v-container>
    <div ref="chart" class="chart-container"></div>
  </v-container>
</template>

<script>
import * as d3 from 'd3';

export default {
  name: 'BarChart',
  data() {
    return {
      data: [30, 86, 168, 281, 303, 365]
    };
  },
  mounted() {
    this.$nextTick(() => {
      this.drawChart();
      window.addEventListener('resize', this.handleResize);
    });
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.handleResize);
  },
  methods: {
    handleResize() {
      this.drawChart();
    },
    drawChart() {
      const element = this.$refs.chart;
      if (!element) return;

      const data = this.data;
      const margin = { top: 20, right: 30, bottom: 40, left: 40 };
      const width = element.clientWidth - margin.left - margin.right;
      const height = element.clientHeight - margin.top - margin.bottom;

      d3.select(element).selectAll('*').remove();

      const svg = d3.select(element)
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      const x = d3.scaleBand()
        .domain(data.map((d, i) => i))
        .range([0, width])
        .padding(0.1);

      const y = d3.scaleLinear()
        .domain([0, d3.max(data)])
        .nice()
        .range([height, 0]);

      svg.append('g')
        .selectAll('rect')
        .data(data)
        .enter().append('rect')
        .attr('x', (d, i) => x(i))
        .attr('y', d => y(d))
        .attr('width', x.bandwidth())
        .attr('height', d => height - y(d))
        .attr('fill', 'steelblue');

      svg.append('g')
        .attr('class', 'x-axis')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(x).tickFormat(i => i + 1));

      svg.append('g')
        .attr('class', 'y-axis')
        .call(d3.axisLeft(y));
    }
  }
}
</script>

<style scoped>
.chart-container {
  width: 100%;
  height: 400px; /* 원하는 높이로 설정 */
}
</style>
