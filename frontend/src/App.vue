<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <!-- Navigation to vue router -->
  <nav>
        <RouterLink to="/market">Market</RouterLink>
        <RouterLink to="/portfolio">Portfolio</RouterLink>
        <RouterLink to="/leaderboard">Leaderboard</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
        <RouterLink to="/register">Register</RouterLink>
    </nav>

  <!-- This shows your pages -->
  <RouterView />

</template>

