

<template>
  
</template>

<script setup lang="ts">

  // import vue-chartjs for top 5 players leaderboard
  import { Bar } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

</script>