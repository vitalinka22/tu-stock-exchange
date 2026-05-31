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
import { onMounted, ref } from 'vue'

// Existing leaderboard chart
import LeaderboardChart from '../components/shared/LeaderboardChart.vue'

// Leaderboard table
import LeaderboardTable from '../components/leaderboard/LeaderboardTable.vue'


// Data for chart
const players = ref<any[]>([])

// Data for table
const users = ref<any[]>([])


// Temporary highlighted user
// TODO: Replace later with logged-in user ID
const currentUserId = 2



// Load leaderboard from backend
onMounted(async () => {

  const response = await fetch(
    'http://localhost:8000/api/leaderboard'
  )

  const data: any[] = await response.json() 

  // Chart data
  players.value = data

users.value = data.map((item: any) => ({
  id: item.user_id,
  username: item.username,
  netWorth: item.portfolio_value
}))

})

</script>