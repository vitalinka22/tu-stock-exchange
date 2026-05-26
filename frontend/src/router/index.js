import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores/auth'

// Import all the pages 
// not found created and imported
import Login from '../pages/Login.vue'
import Register from '../pages/Register.vue'
import Market from '../pages/Market.vue'
import Portfolio from '../pages/Portfolio.vue'
import Leaderboard from '../pages/Leaderboard.vue'
import NotFound from '../pages/NotFound.vue'
import Dashboard from '../pages/Dashboard.vue'
import Default from '../pages/Default.vue'


const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/market', component: Market },
  { path: '/leaderboard', component: Leaderboard },
  { path: '/default', component: Default },

  // meta: { requiresAuth: true } = like @Secured annotation in Spring
  // marks these routes as protected — only logged in users can access them
  { path: '/users/:id/portfolio', component: Portfolio, meta: { requiresAuth: true } },
  //{ path: '/users/:id/portfolio', component: Portfolio },
  { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } },

  { path: '/', redirect: '/market' },  // Default redirect to market
  { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound } //last one should be 404; when nothing else found than 404
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// navigation guard — runs before every route change
// like a servlet filter in Java — intercepts every request
// and checks if the user is allowed to access the route
router.beforeEach((to, from) => {
  const authStore = useAuthStore()

  // if route requires auth AND user is not logged in → redirect to login
  if (to.meta.requiresAuth && !authStore.isLoggedIn) {
    return { path: '/login' }
  }
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