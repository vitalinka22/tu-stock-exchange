<template>
  <div>

    <v-container>

      <div style="max-width: 600px; margin: 0 auto">

        <LeaderboardChart :players="players" />

      </div>


      <br><br>


      <!-- Leaderboard table -->
      <LeaderboardTable
        :users="users"
        :currentUserId="currentUserId"
      />

    </v-container>

  </div>
</template>



<script setup lang="ts">

  // Vue imports
  import { onMounted, ref } from 'vue';

  // Existing leaderboard chart
  import LeaderboardChart from '../components/shared/LeaderboardChart.vue'

  // Added leaderboard table
  import LeaderboardTable from '../components/leaderboard/LeaderboardTable.vue'



  // Existing fake chart data
  // TODO: Replace later with backend API data
  const players = ref([
    { username: 'a_trades', portfolio_value: 42100 },
    { username: 'b_trades', portfolio_value: 38540 },
    { username: 'c_trades', portfolio_value: 31220 },
    { username: 'd_trades', portfolio_value: 27800 },
    { username: 'crypto_carl', portfolio_value: 19500 },
  ])



  // Added fake leaderboard table data
  // TODO: Replace later with backend API data
  const users = ref([

    {
      id: 1,
      username: 'a_trades',
      netWorth: 42100
    },

    {
      id: 2,
      username: 'b_trades',
      netWorth: 38540
    },

    {
      id: 3,
      username: 'c_trades',
      netWorth: 31220
    },

    {
      id: 4,
      username: 'd_trades',
      netWorth: 27800
    },

    {
      id: 5,
      username: 'crypto_carl',
      netWorth: 19500
    }

  ])



  // Current logged-in user
  // Used for highlighted row
  const currentUserId = 2



  // Existing backend example
  // onMounted(async () => {
  //   const response = await fetch('http://localhost:8000/leaderboard')
  //   const data = await response.json()
  //   players.value = data.slice(0, 5)
  // })

</script>