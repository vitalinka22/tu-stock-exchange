import { createRouter, createWebHistory } from 'vue-router'

// Import all the pages 
// not found created and imported
import Login from '../pages/Login.vue'
import Register from '../pages/Register.vue'
import Market from '../pages/Market.vue'
import Portfolio from '../pages/Portfolio.vue'
import Leaderboard from '../pages/Leaderboard.vue'
import NotFound from '../pages/NotFound.vue'

const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/market', component: Market },
  { path: '/portfolio', component: Portfolio },
  { path: '/leaderboard', component: Leaderboard },
  { path: '/', redirect: '/market' },  // Default redirect to market
  { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound } //last one should be 404; when nothing else found than 404
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// notice that the URL of the default Vue app has /#/ suffixed to the URL.
// because the Vue router uses hash mode for routing by default. 
// It uses the URL hash to simulate a full URL so that the page won't be reloaded when the URL changes.
// We can prevent the Vue router from doing this by enabling History mode.

// const router = new VueRouter({
//  mode: 'history',
//  routes
// })

export default router