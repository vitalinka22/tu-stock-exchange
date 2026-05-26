<script setup>
defineProps({
  users: Array, // Array of all leaderboard users
  currentUserId: Number // ID of current logged-in user
})
</script>

<template>
  <table>
    <thead>
      <tr>
        <th>Rank</th>
        <th>User</th>
        <th>Net Worth</th>
      </tr>
    </thead>

    <tbody>
      <tr
        v-for="(user, index) in users"
        :key="user.id"
        :class="{ highlighted: user.id === currentUserId }"
      >
        <td>{{ index + 1 }}</td>
        <td>{{ user.username }}</td>
        <td>${{ user.netWorth }}</td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped>
table {
  width: 70%;
  margin: 0 auto;
  border-collapse: collapse;
}

th,
td {
  padding: 12px;
  border-bottom: 1px solid #ddd;
}

.highlighted {
  background-color: #2563eb;
  color: white;
}
</style>


