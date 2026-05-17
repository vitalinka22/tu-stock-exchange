import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '../api/axiosInstance'

export const useAuthStore = defineStore('auth', () => {
  // STATE - shared memory (what we store)
  const token = ref(localStorage.getItem('token') || null)
  const user = ref(null)

  // GETTERS - computed values based on state
  const isLoggedIn = computed(() => !!token.value) // true if token exists

  // ACTIONS - functions that change the state
  async function login(username, password) {
    // IGOR: added mock login for testing before backend is ready
    // remove this block once Anastasia's backend is deployed
    if (username === 'testuser' && password === 'Test123!') {
      token.value = 'mock-token-123'
      localStorage.setItem('token', token.value)
      user.value = { username: 'testuser' }
      return
    }

    // real API call — will work once backend is deployed
    const response = await api.post('/auth/login', { username, password })
    token.value = response.data.token         // save token to memory
    localStorage.setItem('token', token.value) // save token to browser
    user.value = response.data.user            // save user data
  }

  function logout() {
    token.value = null  // clear token from memory
    user.value = null   // clear user data
    localStorage.removeItem('token') // clear token from browser
    window.location.href = '/login'  // redirect to login page
  }

  return { token, user, isLoggedIn, login, logout }
})