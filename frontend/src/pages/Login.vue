<template>

  <v-container fluid class="login-background d-flex align-center justify-center" style="min-height: 100vh" >

    <v-card
      width="420"
      class="pa-8 login-card"
      elevation="0"
      rounded="xl"
    >
      <v-card-title class="text-h5 font-weight-bold pb-1">
        Welcome back
      </v-card-title>

      <v-card-subtitle class="mb-3">
          Please enter your details
      </v-card-subtitle>

      <v-card-text>

        <v-form ref="form">

          <v-text-field
            class="mb-3"
            v-model="email"
            :rules="emailRules"
            label="Email"
            type="email"
            variant="outlined"
            rounded="lg"
            density="comfortable"
            prepend-inner-icon="mdi-email-outline"
          />

          <v-text-field
            class="mb-3" 
            v-model="password"
            :rules="passwordRules"
            label="Password"
            type="password"
            variant="outlined"
            rounded="lg"
            density="comfortable"
            prepend-inner-icon="mdi-lock-outline"
          />

          <div class="d-flex align-center justify-space-between">
              <label class="d-flex align-center ga-2">
                <input type="checkbox" v-model="rememberMe" />
                Remember me
              </label>

              <RouterLink
                to="/forgot-password"
                class="signup-link ml-1"
              >
                Forgot password
              </RouterLink>

            </div>

          <v-alert v-if="errorMessage" type="error" 
            variant="tonal"
            rounded="lg"
            class="mt-2"
          >
            {{ errorMessage }}
          </v-alert>

        </v-form>
      </v-card-text>

      <v-card-actions  class="flex-column align-stretch">

        <v-btn
          block
          size="large"
          color="indigo-darken-3"
          @click="onSubmit"
          variant="flat"
          :loading="loading"
          class="mt-4 text-none font-weight-bold"
          rounded="lg"
        >
          Sign in
        </v-btn>

        <div class="d-flex align-center justify-center mt-4 ga-1">
          <span class="text-medium-emphasis">
            Don't have an account?
          </span>

          <RouterLink
            to="/register"
            class="signup-link ml-1"
          >
            Sign up
          </RouterLink>
        </div>
      
      </v-card-actions>

    </v-card>
   
  </v-container>

</template>

<script setup lang="ts">
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { useAuthStore } from '@/stores/auth' // IGOR: imported auth store to handle real login

  const email = ref('')
  const password = ref('')
  const loading = ref(false)
  const errorMessage = ref('')
  const rememberMe = ref(false)
  const form = ref<{ validate: () => Promise<{ valid: boolean }> } | null>(null)

  const router = useRouter()
  const authStore = useAuthStore()

  const emailRules = [
    (v: string) => !!v || 'Email required',
    (v: string) => /.+@.+\..+/.test(v) || 'Email must be valid'
  ]

  const passwordRules = [
    (v: string) => !!v || 'Password required',
    (v: string) => v.length >= 8 || 'Minimum 8 characters',
    (v: string) => /[a-z]/.test(v) || 'At least 1 lowercase letter',
    (v: string) => /[A-Z]/.test(v) || 'At least 1 uppercase letter',
    (v: string) => /[\d\W]/.test(v) || 'At least 1 number or special character'
  ]

  async function onSubmit() {
    if (!form.value) return
    const { valid } = await form.value.validate()
    if (!valid) return

    loading.value = true
    errorMessage.value = ''

    try {
      // IGOR: replaced fake setTimeout with real API call
      // authStore.login() calls POST /auth/login and saves token to localStorage
      await authStore.login(email.value, password.value)

      // IGOR: redirect to dashboard after successful login (was redirecting to '/')
      router.push('/dashboard')

    } catch (error) {
      // IGOR: shows error if API call fails (wrong credentials or backend down)
      errorMessage.value = 'Invalid username or password'
    } finally {
      loading.value = false
    }
  }
</script>

<style scoped>
  .login-card {
    border: 1px solid #ececec;
    box-shadow: 0 10px 40px rgba(0,0,0,0.08);
  }

  .login-background {
    min-height: 100vh;
    background:
      radial-gradient(circle at top left, #e0e7ff, transparent 30%),
      radial-gradient(circle at bottom right, #c7d2fe, transparent 30%),
      #f5f7fb;
  }

  .signup-link {
    color: #283593;
    text-decoration: none;
    font-weight: 500;
  }
</style>