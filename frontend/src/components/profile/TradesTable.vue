
<script setup>

import { ref, computed } from "vue"


// Fake trade history data - Will be replaced later by backend API data
const trades = [

  {
    id: 1,
    type: "BUY",
    stock: "AAPL",
    shares: 5,
    price: 190
  },

  {
    id: 2,
    type: "SELL",
    stock: "TSLA",
    shares: 2,
    price: 220
  },

  {
    id: 3,
    type: "BUY",
    stock: "NVDA",
    shares: 1,
    price: 800
  }
]


// Current selected filter
const filter = ref("ALL")


// Filtered trades
const filteredTrades = computed(() => {

  // Show everything
  if (filter.value === "ALL") {
    return trades
  }

  // Show only matching trades
  return trades.filter(
    trade => trade.type === filter.value
  )
})

</script>



<template>

  <div>

   
    <select v-model="filter">

      <option value="ALL">ALL</option>

      <option value="BUY">BUY</option>

      <option value="SELL">SELL</option>

    </select>



   
    <table>

      <thead>
        <tr>
          <th>Type</th>
          <th>Stock</th>
          <th>Shares</th>
          <th>Price</th>
        </tr>
      </thead>



      <tbody>

     
        <tr
          v-for="trade in filteredTrades"
          :key="trade.id"
        >

          <td>{{ trade.type }}</td>

          <td>{{ trade.stock }}</td>

          <td>{{ trade.shares }}</td>

          <td>${{ trade.price }}</td>

        </tr>

      </tbody>

    </table>

  </div>

</template>



<style scoped>

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th,
td {
  padding: 12px;
  border-bottom: 1px solid #ddd;
  text-align: left;
}

select {
  padding: 8px;
}

</style>