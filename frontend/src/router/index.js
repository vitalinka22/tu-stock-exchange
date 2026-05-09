import { createRouter, createWebHistory } from 'vue-router'

// Import your pages (create these next)
import Login from '../pages/Login.vue'
import Register from '../pages/Register.vue'
import Market from '../pages/Market.vue'
import Portfolio from '../pages/Portfolio.vue'
import Leaderboard from '../pages/Leaderboard.vue'

const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/market', component: Market },
  { path: '/portfolio', component: Portfolio },
  { path: '/leaderboard', component: Leaderboard },
  { path: '/', redirect: '/market' }  // Default redirect to market
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router