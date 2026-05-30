 <template>


  <!-- lucide icon added for title-->
  <div class="mb-10 flex items-center justify-center gap-3">

    <div class="flex items-center justify-center w-12 h-12 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl shadow-lg">
      <TrendingUp :size="24" class = "market-page" />
    </div>

    <h1 class="text-h4 font-weight-bold pb-1 text-white">Market</h1>

    <div class="flex items-center justify-center w-12 h-12 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl shadow-lg">
      <TrendingUp :size="24" class = "market-page" />
    </div>

  </div>



  <!-- lucide icon added; the search icon and search bar have to be in the same container -->
  <div class="flex items-center border border-gray-700 bg-gradient-to-br from-gray-900 to-blue-950 rounded-2xl mb-6  transition-all">
    <Search :size="20" class="text-gray-400 ml-3 flex-shrink-0" />
    
    <input
      v-model="search"
      type="text"
      placeholder="Search stocks..."
      class="bg-transparent text-white p-3 w-full focus:outline-none placeholder-gray-400"
    />

  </div>


    <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6 ">
      <div
      v-for="stock in filteredStocks"
      :key="stock.symbol"
      class="w-full border border-gray-700 rounded-2xl p-6 shadow-md hover:shadow-xl transition bg-gradient-to-br from-gray-900 to-blue-950 ">
        <div class="flex gap-3 mb-4">
    
          <div >
            <h2 class="font-bold text-3xl">{{ stock.symbol }}</h2>
            <p class="text-gray-400 text-lg">{{ stock.name }}</p>

          
          </div>

          

            <button
              class="hover:scale-110 transition"
            >
              <Star class="w-4 h-4 text-yellow-400" />
            </button>
          

          



        </div>

        <div class="mt-6">

          <p class="font-bold text-2xl text-white text-left">
            ${{ stock.price }}
          </p>


          <div class="flex gap-3 mb-4">

            <!-- lucide icon for both buttons added-->
            <button
              @click="buyStock(stock.symbol)"
              class="bg-green-500 hover:bg-green-600 transition text-white px-5 py-2 rounded-xl flex items-center justify-center gap-2 min-w-[140px]"
              :class="{ 'opacity-80': !authStore.isLoggedIn }">
              

              <span class="font-bold tracking-wide">Buy</span>
              <ShoppingCart class="w-4 h-4" />

            </button>
          
          
            <button
                @click="sellStock(stock.symbol)"
                class="bg-red-500 hover:bg-red-600 transition text-white px-5 py-2 rounded-xl  flex items-center justify-center gap-2 min-w-[140px]"
                :class="{ 'opacity-80': !authStore.isLoggedIn }">
             
                <span class="font-bold tracking-wide">Sell</span>
                <ArrowDownToLine class="w-4 h-4" />
                 
              </button>

             
            
          </div>
  

        </div>

    </div>

  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue"
import {useAuthStore} from "@/stores/auth"

// lucide icons
import { Search,
        TrendingUp,
        ArrowDownToLine,
        ShoppingCart,
        Star 
 } from 'lucide-vue-next'

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

