<script setup lang="ts">

// Access route parameters
import { useRoute } from "vue-router"


// Import your existing components
import NetWorthChart from "@/components/profile/NetWorthChart.vue"
import TradesTable from "@/components/profile/TradesTable.vue"


// Current route
const route = useRoute()


// Get user ID from URL
const userId = route.params.id

</script>



<template>

  <div class="p-8">

    <!-- Page title -->
    <h1 class="text-2xl font-bold">
      Public Portfolio
    </h1>


    <!-- Current viewed user -->
    <p>
      Viewing portfolio of user:
      {{ userId }}
    </p>


    <br>


    <!-- Net worth history -->
    <NetWorthChart />


    <br><br>


    <!-- Trades history -->
    <TradesTable />

  </div>

</template>