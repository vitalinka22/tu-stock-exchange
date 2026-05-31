<template>
  <div class="p-8 w-full max-w-5xl mx-auto">
    <h1 class="text-4xl font-bold mb-2 text-white">Auto-trades</h1>
    <p class="text-sm mb-10 text-yellow-600 uppercase tracking-widest font-medium">Automatic orders</p>

    <!-- create form -->
    <div class="rounded-xl bg-zinc-900 border border-zinc-800 p-6 mb-8">
      <h2 class="text-base font-semibold text-white uppercase tracking-widest mb-6">New auto-trade</h2>
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-4">
        <div>
          <label class="text-xs text-zinc-500 uppercase tracking-widest">Ticker</label>
          <input
            v-model="form.ticker"
            type="text"
            placeholder="e.g. AAPL"
            class="mt-2 w-full p-3 rounded-xl bg-zinc-800 border border-zinc-700 text-white uppercase focus:outline-none focus:ring-2 focus:ring-yellow-500"
          />
        </div>
        <div>
          <label class="text-xs text-zinc-500 uppercase tracking-widest">Type</label>
          <select
            v-model="form.trade_type"
            class="mt-2 w-full p-3 rounded-xl bg-zinc-800 border border-zinc-700 text-white focus:outline-none focus:ring-2 focus:ring-yellow-500"
          >
            <option value="buy">Buy</option>
            <option value="sell">Sell</option>
          </select>
        </div>
        <div>
          <label class="text-xs text-zinc-500 uppercase tracking-widest">Target price ($)</label>
          <input
            v-model.number="form.target_price"
            type="number"
            min="0.01"
            step="0.01"
            class="mt-2 w-full p-3 rounded-xl bg-zinc-800 border border-zinc-700 text-white focus:outline-none focus:ring-2 focus:ring-yellow-500"
          />
        </div>
        <div>
          <label class="text-xs text-zinc-500 uppercase tracking-widest">Quantity</label>
          <input
            v-model.number="form.quantity"
            type="number"
            min="1"
            class="mt-2 w-full p-3 rounded-xl bg-zinc-800 border border-zinc-700 text-white focus:outline-none focus:ring-2 focus:ring-yellow-500"
          />
        </div>
      </div>

      <p v-if="form.error" class="text-red-400 text-sm mb-3">{{ form.error }}</p>
      <p v-if="form.success" class="text-emerald-400 text-sm mb-3">{{ form.success }}</p>

      <button
        @click="createAutoTrade"
        :disabled="form.loading"
        class="bg-yellow-600 hover:bg-yellow-700 text-white font-semibold px-6 py-3 rounded-xl transition"
      >
        {{ form.loading ? 'Creating...' : 'Create auto-trade' }}
      </button>
    </div>

    <!-- active auto-trades list -->
    <div class="rounded-xl bg-zinc-900 border border-zinc-800 overflow-hidden">
      <div class="px-6 py-5 border-b border-zinc-800 flex items-center justify-between">
        <h2 class="text-base font-semibold text-white uppercase tracking-widest">Active auto-trades</h2>
        <span class="text-xs text-yellow-600 uppercase tracking-widest">{{ autoTrades.length }} active</span>
      </div>

      <div v-if="loading" class="p-6 text-zinc-500">Loading...</div>
      <div v-else-if="error" class="p-6 text-red-400">{{ error }}</div>
      <p v-else-if="autoTrades.length === 0" class="p-6 text-zinc-500">No active auto-trades yet.</p>

      <table v-else class="w-full">
        <thead>
          <tr class="text-left border-b border-zinc-800">
            <th class="px-6 py-3 text-xs uppercase tracking-widest text-zinc-500">Ticker</th>
            <th class="px-6 py-3 text-xs uppercase tracking-widest text-zinc-500">Type</th>
            <th class="px-6 py-3 text-xs uppercase tracking-widest text-zinc-500">Target price</th>
            <th class="px-6 py-3 text-xs uppercase tracking-widest text-zinc-500">Quantity</th>
            <th class="px-6 py-3 text-xs uppercase tracking-widest text-zinc-500"></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="at in autoTrades"
            :key="at.id"
            class="border-b border-zinc-800 hover:bg-zinc-800 transition"
          >
            <td class="px-6 py-4 font-bold text-yellow-500">{{ at.ticker }}</td>
            <td class="px-6 py-4">
              <span
                class="px-2 py-1 rounded-lg text-xs font-semibold uppercase"
                :class="at.trade_type === 'buy' ? 'bg-green-900/50 text-green-400' : 'bg-red-900/50 text-red-400'"
              >{{ at.trade_type }}</span>
            </td>
            <td class="px-6 py-4 text-zinc-300">${{ at.target_price?.toFixed(2) }}</td>
            <td class="px-6 py-4 text-zinc-300">{{ at.quantity }}</td>
            <td class="px-6 py-4">
              <button
                @click="deleteAutoTrade(at.id)"
                class="text-red-400 hover:text-red-300 text-sm transition"
              >Cancel</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api/axiosInstance'

const autoTrades = ref([])
const loading = ref(true)
const error = ref(null)

const form = ref({
  ticker: '',
  trade_type: 'buy',
  target_price: 0,
  quantity: 1,
  loading: false,
  error: null,
  success: null,
})

async function fetchAutoTrades() {
  try {
    const response = await api.get('/auto-trades')
    autoTrades.value = response.data.auto_trades
  } catch (e) {
    error.value = 'Could not load auto-trades.'
  } finally {
    loading.value = false
  }
}

async function createAutoTrade() {
  form.value.error = null
  form.value.success = null

  if (!form.value.ticker || form.value.target_price <= 0 || form.value.quantity < 1) {
    form.value.error = 'Please fill in all fields correctly.'
    return
  }

  form.value.loading = true
  try {
    await api.post('/auto-trades', {
      ticker: form.value.ticker.toUpperCase(),
      trade_type: form.value.trade_type,
      target_price: form.value.target_price,
      quantity: form.value.quantity,
    })
    form.value.success = 'Auto-trade created!'
    form.value.ticker = ''
    form.value.target_price = 0
    form.value.quantity = 1
    await fetchAutoTrades()
  } catch (e) {
    form.value.error = e.response?.data?.detail ?? 'Failed to create auto-trade.'
  } finally {
    form.value.loading = false
  }
}

async function deleteAutoTrade(id) {
  try {
    await api.delete(`/auto-trades/${id}`)
    autoTrades.value = autoTrades.value.filter(at => at.id !== id)
  } catch (e) {
    error.value = 'Could not cancel auto-trade.'
  }
}

onMounted(fetchAutoTrades)
</script>
