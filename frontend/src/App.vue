<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <nav class="w-full flex items-center gap-6 px-10 py-4 border-b border-zinc-800 bg-zinc-950">
    <span class="text-white font-bold text-lg mr-4">TU Stock Exchange</span>
    <RouterLink to="/market" class="text-gray-400 hover:text-white transition">Market</RouterLink>
    <RouterLink to="/portfolio" class="text-gray-400 hover:text-white transition">Portfolio</RouterLink>
    <RouterLink to="/leaderboard" class="text-gray-400 hover:text-white transition">Leaderboard</RouterLink>
    <RouterLink to="/dashboard" class="text-gray-400 hover:text-white transition">Dashboard</RouterLink>
    <div class="ml-auto flex gap-4">
      <RouterLink to="/login" class="text-gray-400 hover:text-white transition">Login</RouterLink>
      <RouterLink to="/register" class="text-gray-400 hover:text-white transition">Register</RouterLink>
    </div>
  </nav>

  <main class="min-h-screen bg-zinc-950 text-white">
    <RouterView />
  </main>
</template>