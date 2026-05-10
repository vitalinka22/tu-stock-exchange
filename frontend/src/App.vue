<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <!-- Navigation to vue router -->
      <nav>
        <RouterLink to="/market">Market</RouterLink>
        <RouterLink to="/portfolio">Portfolio</RouterLink>
        <RouterLink to="/leaderboard">Leaderboard</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
        <RouterLink to="/register">Register</RouterLink>
      </nav>
    </div>
  </header>

  <!-- This shows your pages -->
  <RouterView />

  <!-- You can delete this when you start working -->
   <div>
    <div style="background: yellow; padding: 10px; border: 2px solid red;">
      <h1>🚀 APP.VUE IS LOADED! 🚀</h1>
      <p>If you see this yellow box, Vue is working!</p>
    </div>
    
    <nav style="background: #333; padding: 10px; color: white;">
      <RouterLink to="/market" style="color: white; margin-right: 10px;">Market</RouterLink>
      <RouterLink to="/login" style="color: white;">Login</RouterLink>
    </nav>
    
    <div style="background: lightblue; padding: 20px; margin: 10px; border: 2px solid blue;">
      <h2>RouterView below this line</h2>
      <hr />
      <RouterView />
      <hr />
      <h2>RouterView above this line</h2>
    </div>
  </div>

  <v-container>
    <v-btn color="primary">
      Vuetify funktioniert!
    </v-btn>
  </v-container>
    <!-- delete until here -->


  <main>
    <TheWelcome />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  margin: 1rem 0;
  display: flex;
  gap: 1rem;
  justify-content: center;
}

nav a {
  color: #42b983;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: 0.2s;
}

nav a:hover {
  background-color: #42b98320;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>