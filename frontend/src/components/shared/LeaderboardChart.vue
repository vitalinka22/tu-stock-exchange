<template>
    <Bar 
    :data = "chartData"
    :options = "chartOptions"
    />
  
</template>

<script setup lang="ts">


    import { computed } from 'vue'

    // import vue-chartjs for top 5 players leaderboard
    import { Bar } from 'vue-chartjs'
    import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

    ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

    // props
    const props = defineProps<{
        players: { username: string, portfolio_value: number }[]
    }>()

    const chartData = computed(() => ({
        labels: props.players.map(p => p.username),
        datasets: [{
            label: 'Portfolio Value',
            data: props.players.map(p => p.portfolio_value),
            backgroundColor: ['#7C3AED', '#9F67F5', '#B48AF7', '#C9A8F9', '#E4D3FC']
        }]
    }))

    const chartOptions = {
        responsive: true,
        plugins: {
            legend: { display: false },
            title: {
                display: true,
                text: 'Top 5 Players'
            }
        }
        
    }

</script>