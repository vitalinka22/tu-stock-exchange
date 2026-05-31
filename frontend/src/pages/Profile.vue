<template>
  <div class="p-8 w-full max-w-5xl mx-auto">
    <h1 class="text-4xl font-bold mb-2 text-white">Profile</h1>
    <p class="text-sm mb-10 text-yellow-600 uppercase tracking-widest font-medium">Your account</p>

    <div v-if="loading" class="text-zinc-400">Loading...</div>
    <div v-else-if="error" class="text-red-400">{{ error }}</div>

    <div v-else>
      <!-- user info cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <div class="rounded-xl p-6 bg-zinc-900 border border-zinc-800">
          <p class="text-xs uppercase tracking-widest text-zinc-500 mb-3">Username</p>
          <p class="text-2xl font-semibold text-white">{{ user?.username ?? '—' }}</p>
        </div>
        <div class="rounded-xl p-6 bg-zinc-900 border border-zinc-800">
          <p class="text-xs uppercase tracking-widest text-zinc-500 mb-3">Cash balance</p>
          <p class="text-2xl font-semibold text-white">${{ networth?.cash_balance?.toFixed(2) ?? '—' }}</p>
        </div>
        <div class="rounded-xl p-6 bg-zinc-900 border border-zinc-800">
          <p class="text-xs uppercase tracking-widest text-zinc-500 mb-3">Net worth</p>
          <p class="text-2xl font-semibold text-white">${{ networth?.networth?.toFixed(2) ?? '—' }}</p>
        </div>
      </div>

      <!-- trades history -->
      <div class="rounded-xl bg-zinc-900 border border-zinc-800 overflow-hidden">
        <div class="px-6 py-5 border-b border-zinc-800 flex items-center justify-between">
          <h2 class="text-base font-semibold text-white uppercase tracking-widest">Trade history</h2>
          <div class="flex gap-3">
            <button
              @click="filter = ''"
              class="text-xs uppercase tracking-widest px-3 py-1 rounded-lg transition"
              :class="filter === '' ? 'bg-yellow-600 text-white' : 'text-zinc-400 hover:text-white'"
            >All</button>
            <button
              @click="filter = 'buy'"
              class="text-xs uppercase tracking-widest px-3 py-1 rounded-lg transition"
              :class="filter === 'buy' ? 'bg-green-700 text-white' : 'text-zinc-400 hover:text-white'"
            >Buy</button>
            <button
              @click="filter = 'sell'"
              class="text-xs uppercase tracking-widest px-3 py-1 rounded-lg transition"
              :class="filter === 'sell' ? 'bg-red-700 text-white' : 'text-zinc-400 hover:text-white'"
            >Sell</button>
            <button
              @click="exportCSV"
              class="text-xs uppercase tracking-widest px-3 py-1 rounded-lg bg-zinc-700 text-zinc-300 hover:bg-zinc-600 transition"
            >Export CSV</button>
          </div>
        </div>

        <p v-if="filteredTrades.length === 0" class="p-6 text-zinc-500">No trades yet.</p>

        <table v-else class="w-full">
          <thead>
            <tr class="text-left border-b border-zinc-800">
              <th class="px-6 py-3 text-xs uppercase tracking-widest text-zinc-500">Date</th>
              <th class="px-6 py-3 text-xs uppercase tracking-widest text-zinc-500">Ticker</th>
              <th class="px-6 py-3 text-xs uppercase tracking-widest text-zinc-500">Type</th>
              <th class="px-6 py-3 text-xs uppercase tracking-widest text-zinc-500">Qty</th>
              <th class="px-6 py-3 text-xs uppercase tracking-widest text-zinc-500">Price</th>
              <th class="px-6 py-3 text-xs uppercase tracking-widest text-zinc-500">Total</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="trade in filteredTrades"
              :key="trade.id"
              class="border-b border-zinc-800 hover:bg-zinc-800 transition"
            >
              <td class="px-6 py-4 text-zinc-400 text-sm">{{ formatDate(trade.timestamp) }}</td>
              <td class="px-6 py-4 font-bold text-yellow-500">{{ trade.ticker }}</td>
              <td class="px-6 py-4">
                <span
                  class="px-2 py-1 rounded-lg text-xs font-semibold uppercase"
                  :class="trade.trade_type === 'buy' ? 'bg-green-900/50 text-green-400' : 'bg-red-900/50 text-red-400'"
                >{{ trade.trade_type }}</span>
              </td>
              <td class="px-6 py-4 text-zinc-300">{{ trade.quantity }}</td>
              <td class="px-6 py-4 text-zinc-300">${{ trade.price?.toFixed(2) }}</td>
              <td class="px-6 py-4 text-white font-medium">${{ trade.total_value?.toFixed(2) }}</td>
            </tr>
          </tbody>
        </table>

        <!-- pagination -->
        <div class="px-6 py-4 border-t border-zinc-800 flex items-center justify-between">
          <button
            @click="prevPage"
            :disabled="page === 1"
            class="text-sm text-zinc-400 hover:text-white disabled:opacity-40 transition"
          >← Previous</button>
          <span class="text-xs text-zinc-500">Page {{ page }}</span>
          <button
            @click="nextPage"
            :disabled="trades.length < limit"
            class="text-sm text-zinc-400 hover:text-white disabled:opacity-40 transition"
          >Next →</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useAuthStore } from '@/stores/auth'
import api from '@/api/axiosInstance'

const authStore = useAuthStore()
const user = computed(() => authStore.user)

const trades = ref([])
const networth = ref(null)
const loading = ref(true)
const error = ref(null)
const filter = ref('')
const page = ref(1)
const limit = 10

const filteredTrades = computed(() =>
  filter.value ? trades.value.filter(t => t.trade_type === filter.value) : trades.value
)

async function fetchTrades() {
  const response = await api.get('/trades/history', { params: { page: page.value, limit } })
  trades.value = response.data.trades
}

async function fetchNetworth() {
  const response = await api.get('/portfolio/networth')
  networth.value = response.data
}

onMounted(async () => {
  try {
    await Promise.all([fetchTrades(), fetchNetworth()])
  } catch (e) {
    error.value = 'Failed to load profile data.'
  } finally {
    loading.value = false
  }
})

watch(page, fetchTrades)

function prevPage() {
  if (page.value > 1) page.value--
}
function nextPage() {
  if (trades.value.length === limit) page.value++
}

function formatDate(ts) {
  if (!ts) return '—'
  return new Date(ts).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' })
}

function exportCSV() {
  if (!trades.value.length) return
  const header = 'Date,Ticker,Type,Quantity,Price,Total'
  const rows = trades.value.map(t =>
    `${formatDate(t.timestamp)},${t.ticker},${t.trade_type},${t.quantity},${t.price},${t.total_value}`
  )
  const csv = [header, ...rows].join('\n')
  const blob = new Blob([csv], { type: 'text/csv' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'trades.csv'
  a.click()
  URL.revokeObjectURL(url)
}
</script>
