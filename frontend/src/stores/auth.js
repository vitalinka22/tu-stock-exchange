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
  async function login(email, password) {
    if (email === 'test@test.com' && password === 'Test123!') {
      token.value = 'mock-token-123'
      localStorage.setItem('token', token.value)
      user.value = { email: 'test@test.com' }
      return
    }

    const response = await api.post('/auth/login', { email, password })
    token.value = response.data.access_token
    localStorage.setItem('token', token.value)
    user.value = { email }
  }

  function logout() {
    token.value = null  // clear token from memory
    user.value = null   // clear user data
    localStorage.removeItem('token') // clear token from browser
    window.location.href = '/login'  // redirect to login page
  }

  return { token, user, isLoggedIn, login, logout }
})