 <template>
  <div class="p-8 w-full">
    <div class="mb-10">
    <h1 class="text-5xl font-bold mb-6">Market</h1>

    <input
      v-model="search"
      type="text"
      placeholder="Search stocks..."
      class="border border-gray-700 bg-gradient-to-br from-gray-900 to-blue-950 text-white p-3 rounded-2xl w-full mb-6 focus:outline-none focus:ring-2 focus:ring-blue-500"
    />
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
      <div
      v-for="stock in filteredStocks"
      :key="stock.symbol"
      class="w-full border border-gray-700 rounded-2xl p-6 shadow-md hover:shadow-xl transition bg-gradient-to-br from-gray-900 to-blue-950">
    <div class="flex justify-between items-start">
    
    <div>
      <h2 class="font-bold text-3xl">{{ stock.symbol }}</h2>
      <p class="text-gray-400 text-lg">{{ stock.name }}</p>
    </div>

    <p class="font-bold text-2xl">${{ stock.price }}</p>
  </div>

  <div class="mt-6 flex gap-3">
    
    <button
      @click="buyStock(stock.symbol)"
      class="bg-green-500 hover:bg-green-600 transition text-white px-5 py-2 rounded-xl"
      :class="{ 'opacity-50': !authStore.isLoggedIn }">
      Buy
    </button>

    <button
      @click="sellStock(stock.symbol)"
      class="bg-red-500 hover:bg-red-600 transition text-white px-5 py-2 rounded-xl"
      :class="{ 'opacity-50': !authStore.isLoggedIn }">
      Sell
    </button>
        
       </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue"
import {useAuthStore} from "@/stores/auth"

const search = ref("")
const authStore = useAuthStore()

const stocks = ref([
  {symbol: "AAPL", name: "Apple", price: 210},
  {symbol: "TSLA", name: "Tesla", price: 180},
  {symbol: "MSFT", name: "Microsoft", price: 425},
  {symbol: "AMZN", name: "Amazon", price: 190},])

const filteredStocks = computed(() => {
  return stocks.value.filter(stock =>
    stock.name.toLowerCase().includes(search.value.toLowerCase()) ||
    stock.symbol.toLowerCase().includes(search.value.toLowerCase()))})

const buyStock = (symbol: string) => {
  if(!authStore.isLoggedIn){
  alert("Please login to trade stocks")
  window.location.href = "/login"
  return
  }
  alert('Buying ${symbol}')
}

const sellStock = (symbol: string) => {
  if(!authStore.isLoggedIn){
  alert("Please login to trade stocks")
  window.location.href = "/login"
  return
  }
  alert(`Selling ${symbol}`)
}


</script>