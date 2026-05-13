<template>

  <v-container fluid class="login-background align-center justify-center" style="min-height: 100vh" >

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
            v-model="username"
            :rules="usernameRules"
            label="Username"
            type="type"
            variant="outlined"
            rounded="lg"
            density="comfortable"
            prepend-inner-icon="mdi-account-outline"
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

        <!-- class="flex-column align-stretch": buttons are one under the other-->        
        <!-- class="justify-space-between" offers space between buttons-->
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

  const username = ref('')
  const password = ref('')
  const loading = ref(false)
  const errorMessage = ref('')
  const rememberMe =ref(false)
  const form = ref<{ validate: () => Promise<{ valid: boolean }> } | null>(null)

  const router = useRouter() 

  
  const usernameRules = [
    (v: string) => !!v || 'Username required',
    (v: string) => v.length >= 5 || 'Minimum 5 characters' ,
    (v: string) => v.length <= 20 || 'Maximum 20 characters',
    (v: string) => /^[a-zA-Z0-9_]+$/.test(v) || 'Only letters, numbers, and underscores allowed',
    (v: string) => !v.includes(' ') || 'Spaces are not allowed'
  ]

  const passwordRules = [
    (v: string) => !!v || 'Password required',
    (v: string) => v.length >= 8 || 'Minimum 8 characters' ,
    (v: string) => /[a-z]/.test(v) || 'At least 1 lowercase letter',
    (v: string) => /[A-Z]/.test(v) || 'At least 1 uppercase letter',
    (v: string) => /[\d\W]/.test(v) || 'At least 1 number or special character'
  ]

  async function onSubmit() {
    if (!form.value) return
    const { valid } = await form.value.validate()
    if (!valid ) return
    loading.value= true

    try {
   
      await new Promise(resolve => setTimeout(resolve, 1000))
      
      router.push('/')
    
      } catch (error) {
        errorMessage.value = 'Invalid email or password'
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