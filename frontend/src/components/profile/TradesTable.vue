<script setup>

import { ref, computed } from "vue"


// Fake trade history data
// TODO: Replace later with backend API data
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

  // Show all trades
  if (filter.value === "ALL") {
    return trades
  }

  // Show only matching trades
  return trades.filter(
    trade => trade.type === filter.value
  )
})



// Export trades into CSV file
function exportCSV() {

  // CSV rows
  const rows = [

    // Table headers
    ["Type", "Stock", "Shares", "Price"],


    // Trade data
    ...filteredTrades.value.map(trade => [
      trade.type,
      trade.stock,
      trade.shares,
      trade.price
    ])
  ]


  // Convert rows into CSV text
  const csvContent = rows
    .map(row => row.join(","))
    .join("\n")


  // Create downloadable file
  const blob = new Blob(
    [csvContent],
    { type: "text/csv" }
  )


  // Create temporary download URL
  const url = URL.createObjectURL(blob)


  // Create hidden download link
  const link = document.createElement("a")

  link.href = url

  link.download = "trades.csv"


  // Automatically click link
  link.click()
}

</script>



<template>

  <div>

    <!-- Export CSV button -->
    <button @click="exportCSV">

      Export CSV

    </button>



    <!-- Filter dropdown -->
    <select v-model="filter">

      <option value="ALL">ALL</option>

      <option value="BUY">BUY</option>

      <option value="SELL">SELL</option>

    </select>



    <!-- Trades table -->
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

        <!-- Loop through filtered trades -->
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

button {
  padding: 10px 16px;
  margin-right: 10px;
  cursor: pointer;
  background-color: #4f46e5;
  color: white;
  border: none;
  border-radius: 6px;
}

button:hover {
  background-color: #4338ca;
}

</style>