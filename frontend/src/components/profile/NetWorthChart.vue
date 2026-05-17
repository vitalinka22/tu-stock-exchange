<script setup>

import { Line } from "vue-chartjs"

import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from "chart.js"

ChartJS.register(
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
)


// Fake backend-like data - needs to be replaced later by backend API data
const history = [
  {
    net_worth: 10000,
    timestamp: "2026-05-01"
  },
  {
    net_worth: 12000,
    timestamp: "2026-05-02"
  },
  {
    net_worth: 9000,
    timestamp: "2026-05-03"
  }
]

</script>



<template>

  <Line
    :data="{
      labels: history.map(item => item.timestamp),

      datasets: [
        {
          label: 'Net Worth',

          data: history.map(item => item.net_worth)
        }
      ]
    }"
  />

</template>