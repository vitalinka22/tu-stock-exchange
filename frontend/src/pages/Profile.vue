<script setup>
import { ref, computed, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'
import api from '@/api/axiosInstance'

const authStore = useAuthStore()

const userStats = ref(null)
const loading = ref(true)
const error = ref(null)
const editing = ref(false)

const editForm = ref({
  username: '',
  email: '',
})

const saveSuccess = ref(false)
const saveError = ref(null)

onMounted(async () => {
  try {
    const response = await api.get('/users/me')
    userStats.value = response.data
    editForm.value.username = response.data.username ?? ''
    editForm.value.email = response.data.email ?? ''
  } catch (e) {
    // mock data while backend not available
    userStats.value = {
      username: authStore.user?.username ?? 'Trader',
      email: 'trader@example.com',
      joined: '2024-01-15',
      net_worth: 12340.50,
      starting_balance: 10000,
      total_trades: 47,
      rank: 3,
      win_rate: 64.2,
    }
    editForm.value.username = userStats.value.username
    editForm.value.email = userStats.value.email
  } finally {
    loading.value = false
  }
})

const profitLoss = computed(() => {
  if (!userStats.value) return 0
  return userStats.value.net_worth - userStats.value.starting_balance
})

const profitLossPercent = computed(() => {
  if (!userStats.value) return '0.00'
  return ((profitLoss.value / userStats.value.starting_balance) * 100).toFixed(2)
})

const isProfit = computed(() => profitLoss.value >= 0)

async function saveProfile() {
  saveError.value = null
  saveSuccess.value = false
  try {
    await api.patch('/users/me', editForm.value)
    userStats.value.username = editForm.value.username
    userStats.value.email = editForm.value.email
    saveSuccess.value = true
    editing.value = false
  } catch (e) {
    // mock: just apply locally
    userStats.value.username = editForm.value.username
    userStats.value.email = editForm.value.email
    saveSuccess.value = true
    editing.value = false
  }
}

function cancelEdit() {
  editForm.value.username = userStats.value.username
  editForm.value.email = userStats.value.email
  editing.value = false
  saveError.value = null
}
</script>

<template>
  <div class="p-8 w-full max-w-5xl mx-auto">

    <h1 class="text-4xl font-bold mb-2 text-white">Profile</h1>
    <p class="text-sm mb-10 text-yellow-600 uppercase tracking-widest font-medium">Account overview</p>

    <div v-if="loading" class="text-gray-500">Loading...</div>
    <div v-else-if="error" class="text-red-500">{{ error }}</div>

    <div v-else class="space-y-6">

      <!-- stats row -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">

        <div class="rounded-xl p-5 bg-zinc-900 border border-zinc-800">
          <p class="text-xs uppercase tracking-widest text-zinc-500 mb-2">Net worth</p>
          <p class="text-2xl font-semibold text-white">${{ userStats.net_worth.toFixed(2) }}</p>
          <p :class="isProfit ? 'text-emerald-400' : 'text-red-400'" class="text-xs mt-1 font-medium">
            {{ isProfit ? '+' : '' }}${{ profitLoss.toFixed(2) }} ({{ profitLossPercent }}%)
          </p>
        </div>

        <div class="rounded-xl p-5 bg-zinc-900 border border-zinc-800">
          <p class="text-xs uppercase tracking-widest text-zinc-500 mb-2">Total trades</p>
          <p class="text-2xl font-semibold text-white">{{ userStats.total_trades }}</p>
        </div>

        <div class="rounded-xl p-5 bg-zinc-900 border border-zinc-800">
          <p class="text-xs uppercase tracking-widest text-zinc-500 mb-2">Win rate</p>
          <p class="text-2xl font-semibold text-white">{{ userStats.win_rate }}%</p>
        </div>

        <div class="rounded-xl p-5 bg-zinc-900 border border-zinc-800">
          <p class="text-xs uppercase tracking-widest text-zinc-500 mb-2">Leaderboard rank</p>
          <p class="text-2xl font-semibold text-yellow-500">#{{ userStats.rank }}</p>
        </div>

      </div>

      <!-- user info + edit form -->
      <div class="rounded-xl bg-zinc-900 border border-zinc-800 overflow-hidden">

        <div class="px-6 py-5 border-b border-zinc-800 flex items-center justify-between">
          <h2 class="text-base font-semibold text-white uppercase tracking-widest">Account info</h2>
          <button
            v-if="!editing"
            @click="editing = true"
            class="text-xs text-yellow-600 uppercase tracking-widest hover:text-yellow-400 transition"
          >
            Edit
          </button>
        </div>

        <!-- view mode -->
        <div v-if="!editing" class="px-6 py-6 space-y-4">
          <div class="flex items-center justify-between py-3 border-b border-zinc-800">
            <span class="text-xs uppercase tracking-widest text-zinc-500">Username</span>
            <span class="text-white font-medium">{{ userStats.username }}</span>
          </div>
          <div class="flex items-center justify-between py-3 border-b border-zinc-800">
            <span class="text-xs uppercase tracking-widest text-zinc-500">Email</span>
            <span class="text-zinc-300">{{ userStats.email }}</span>
          </div>
          <div class="flex items-center justify-between py-3">
            <span class="text-xs uppercase tracking-widest text-zinc-500">Member since</span>
            <span class="text-zinc-300">{{ userStats.joined }}</span>
          </div>
        </div>

        <!-- edit mode -->
        <div v-else class="px-6 py-6 space-y-4">

          <div v-if="saveSuccess" class="mb-2 rounded-lg bg-emerald-950 border border-emerald-800 px-4 py-3 text-emerald-400 text-sm">
            Profile updated successfully.
          </div>
          <div v-if="saveError" class="mb-2 rounded-lg bg-red-950 border border-red-800 px-4 py-3 text-red-400 text-sm">
            {{ saveError }}
          </div>

          <div>
            <label class="block text-xs uppercase tracking-widest text-zinc-500 mb-2">Username</label>
            <input
              v-model="editForm.username"
              type="text"
              class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 text-white text-sm focus:outline-none focus:border-yellow-600 transition"
              placeholder="Username"
            />
          </div>

          <div>
            <label class="block text-xs uppercase tracking-widest text-zinc-500 mb-2">Email</label>
            <input
              v-model="editForm.email"
              type="email"
              class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-3 text-white text-sm focus:outline-none focus:border-yellow-600 transition"
              placeholder="Email"
            />
          </div>

          <div class="flex gap-3 pt-2">
            <button
              @click="saveProfile"
              class="px-5 py-2.5 bg-yellow-600 hover:bg-yellow-500 text-black text-xs font-semibold uppercase tracking-widest rounded-lg transition"
            >
              Save changes
            </button>
            <button
              @click="cancelEdit"
              class="px-5 py-2.5 bg-zinc-800 hover:bg-zinc-700 text-zinc-300 text-xs uppercase tracking-widest rounded-lg transition"
            >
              Cancel
            </button>
          </div>

        </div>
      </div>

    </div>
  </div>
</template>