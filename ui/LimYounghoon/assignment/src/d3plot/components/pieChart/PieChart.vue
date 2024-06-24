<template>
  <v-container>
    <div ref="chart" :style="{ width: '100%', height: '500px' }"></div>
  </v-container>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "PieChart",
  data() {
    return {
      chartData: [
        { label: "A", value: 30 },
        { label: "B", value: 20 },
        { label: "C", value: 50 },
      ],
    };
  },
  mounted() {
    this.drawChart();
    window.addEventListener("resize", this.handleResize);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    handleResize() {
      this.clearChart();
      this.drawChart();
    },
    clearChart() {
      d3.select(this.$refs.chart).select("svg").remove();
    },
    drawChart() {
      const width = this.$refs.chart.clientWidth;
      const height = 500;
      const margin = 40;
      const radius = Math.min(width, height) / 2 - margin;

      const svg = d3
        .select(this.$refs.chart)
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", `translate(${width / 2}, ${height / 2})`);

      const color = d3
        .scaleOrdinal()
        .domain(this.chartData.map((d) => d.label))
        .range(d3.schemeCategory10);

      const pie = d3
        .pie()
        .value((d) => d.value)
        .sort(null);

      const arc = d3
        .arc()
        .innerRadius(0)
        .outerRadius(radius);

      const outerArc = d3
        .arc()
        .innerRadius(radius * 1.1)
        .outerRadius(radius * 1.1);

      const arcs = svg
        .selectAll(".arc")
        .data(pie(this.chartData))
        .enter()
        .append("g")
        .attr("class", "arc");

      arcs
        .append("path")
        .attr("d", arc)
        .attr("fill", (d) => color(d.data.label));

      arcs
        .append("text")
        .attr("transform", (d) => {
          const pos = outerArc.centroid(d);
          pos[0] = radius * 1.2 * (midAngle(d) < Math.PI ? 1 : -1);
          return `translate(${pos})`;
        })
        .attr("dy", "0.35em")
        .style("text-anchor", (d) => (midAngle(d) < Math.PI ? "start" : "end"))
        .style("font-size", "24px")
        .text((d) => d.data.label);

      function midAngle(d) {
        return d.startAngle + (d.endAngle - d.startAngle) / 2;
      }

      arcs
        .append("polyline")
        .attr("points", (d) => {
          const pos = outerArc.centroid(d);
          pos[0] = radius * 1.2 * (midAngle(d) < Math.PI ? 1 : -1);
          return [arc.centroid(d), outerArc.centroid(d), pos];
        })
        .style("fill", "none")
        .style("stroke", "black")
        .style("stroke-width", "1px");
    },
  },
};
</script>

<style scoped>
.arc path {
  stroke: #fff;
}

.arc text {
  font-family: Arial, sans-serif;
  font-size: 24px;
  fill: #000;
}

.arc polyline {
  opacity: 0.3;
}
</style>
