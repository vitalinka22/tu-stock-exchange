<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
</script>

<template>
  <nav class="w-full flex items-center gap-6 px-10 py-4 border-b border-zinc-800 bg-zinc-950">
    <span class="text-white font-bold text-lg mr-4">TU Stock Exchange</span>

    <RouterLink to="/market" class="text-gray-400 hover:text-white transition">Market</RouterLink>
    <RouterLink to="/leaderboard" class="text-gray-400 hover:text-white transition">Leaderboard</RouterLink>

    <template v-if="authStore.isLoggedIn">
      <RouterLink to="/dashboard" class="text-gray-400 hover:text-white transition">Dashboard</RouterLink>
      <RouterLink to="/portfolio" class="text-gray-400 hover:text-white transition">Portfolio</RouterLink>
      <RouterLink to="/auto-trades" class="text-gray-400 hover:text-white transition">Auto-trades</RouterLink>
      <RouterLink to="/profile" class="text-gray-400 hover:text-white transition">Profile</RouterLink>
    </template>

    <div class="ml-auto flex gap-4">
      <template v-if="authStore.isLoggedIn">
        <span class="text-zinc-500 text-sm self-center">{{ authStore.user?.username }}</span>
        <button @click="authStore.logout()" class="text-gray-400 hover:text-white transition">Logout</button>
      </template>
      <template v-else>
        <RouterLink to="/login" class="text-gray-400 hover:text-white transition">Login</RouterLink>
        <RouterLink to="/register" class="text-gray-400 hover:text-white transition">Register</RouterLink>
      </template>
    </div>
  </nav>

  <main class="min-h-screen bg-zinc-950 text-white">
    <RouterView />
  </main>
</template>
