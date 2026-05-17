

<template>
  <div>
    <v-container>
      <div style="max-width: 600px; margin: 0 auto">
        <LeaderboardChart :players="players" />
      </div>
  </v-container>
  </div>
  
  
</template>

<script setup lang="ts">

  // prop and function needed for leaderboardchart (top 5 players)
  // fake player; need to coordinate with backend to actually get the top 5 players
  import { onMounted, ref } from 'vue';
  import LeaderboardChart from '../components/shared/LeaderboardChart.vue'

  // const players = ref([])

  const players = ref([
    { username: 'a_trades', portfolio_value: 42100 },
    { username: 'b_trades', portfolio_value: 38540 },
    { username: 'c_trades', portfolio_value: 31220 },
    { username: 'd_trades', portfolio_value: 27800 },
    { username: 'crypto_carl', portfolio_value: 19500 },
  ])

  // in vue it is not async function onMounted()
  // onMounted - code will roll, after the component is mounted; info is received from backend
  // code from backend not working right now so we are using fake names
//   onMounted(async () => {
//    const response = await fetch('http://localhost:8000/leaderboard')
//    const data = await response.json()
//    players.value = data.slice(0, 5)
//  })


</script>