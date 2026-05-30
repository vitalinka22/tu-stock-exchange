<template>

  <v-container fluid class="register-background d-flex align-center justify-center" style="min-height: 100vh">

    <v-card 
      width="420"
      class="pa-8 register-card"
      elevation="0"
      rounded="xl"
    >

      <v-card-title class="text-h5 font-weight-bold pb-1">
        Create Account
      </v-card-title>

      <div class="d-flex align-center justify-space-between">
        <v-card-subtitle class="mb-3">
          Already have an account? 
          <RouterLink to="/login" class="signin-link ml-1">
            Sign in 
          </RouterLink>
        </v-card-subtitle>
      </div>

      <v-card-text>
        <v-form ref="form">

          <v-text-field 
            v-model="email"
            :rules="emailRules"
            label="Email"
            type="email"
            class="mb-3"
            variant="outlined"
            rounded="lg"
            density="comfortable"
          >
            <template v-slot:prepend-inner>
              <Mail :size="20" class="text-grey-darken-1" />
            </template>
          </v-text-field>

          <v-text-field
            v-model="password"
            :rules="passwordRules"
            :type="showPassword ? 'text' : 'password'"
            label="Password"
            class="mb-3"
            variant="outlined"
            rounded="lg"
            density="comfortable"
          >
            <template v-slot:prepend-inner>
              <Lock :size="20" class="text-grey-darken-1" />
            </template>
            <template v-slot:append-inner>
              <Eye 
                v-if="showPassword" 
                :size="18" 
                class="cursor-pointer text-grey-darken-1"
                @click="showPassword = false"
              />
              <EyeOff 
                v-else 
                :size="18" 
                class="cursor-pointer text-grey-darken-1"
                @click="showPassword = true"
              />
            </template>
          </v-text-field>

          <v-text-field
            v-model="confirmPassword"
            :rules="confirmPasswordRules"
            :type="showConfirmPassword ? 'text' : 'password'"
            label="Confirm Password"
            class="mb-3"
            variant="outlined"
            rounded="lg"
            density="comfortable"
          >
            <template v-slot:prepend-inner>
              <Lock :size="20" class="text-grey-darken-1" />
            </template>
            <template v-slot:append-inner>
              <Eye 
                v-if="showConfirmPassword" 
                :size="18" 
                class="cursor-pointer text-grey-darken-1"
                @click="showConfirmPassword = false"
              />
              <EyeOff 
                v-else 
                :size="18" 
                class="cursor-pointer text-grey-darken-1"
                @click="showConfirmPassword = true"
              />
            </template>
          </v-text-field>

          <v-alert v-if="errorMessage" type="error" 
            variant="tonal"
            rounded="lg"
            class="mt-2">
            {{ errorMessage }}
          </v-alert>

        </v-form>
      </v-card-text>

      <v-card-actions class="flex-column align-stretch">

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
          <UserPlus :size="18" class="mr-2" />
          Sign up
        </v-btn>

      </v-card-actions>

    </v-card>
   
  </v-container>

</template>

<script setup lang="ts">
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import api from '@/api/axiosInstance'
  
  import { 
    Mail,      
    Lock,      
    Eye,       
    EyeOff,    
    UserPlus   
  } from 'lucide-vue-next'

  const email = ref('')
  const password = ref('')
  const loading = ref(false)
  const errorMessage = ref('')
  const form = ref<{ validate: () => Promise<{ valid: boolean }> } | null>(null)
  const confirmPassword = ref('')
  
  // Für Password Visibility Toggle
  const showPassword = ref(false)
  const showConfirmPassword = ref(false)

  const router = useRouter()

  const emailRules = [
    (v: string) => !!v || 'Email address required',
    (v: string) => /.+@.+\..+/.test(v) || 'Email must be valid'
  ]

  const passwordRules = [
    (v: string) => !!v || 'Password required',
    (v: string) => v.length >= 8 || 'Minimum 8 characters',
    (v: string) => /[a-z]/.test(v) || 'At least 1 lowercase letter',
    (v: string) => /[A-Z]/.test(v) || 'At least 1 uppercase letter',
    (v: string) => /[\d\W]/.test(v) || 'At least 1 number or special character'
  ]

  const confirmPasswordRules = [
    (v: string) => !!v || 'Please confirm your password',
    (v: string) => v === password.value || 'Passwords do not match'
  ]

  async function onSubmit() {
    if (!form.value) return
    const { valid } = await form.value.validate()
    if (!valid) return

    loading.value = true
    errorMessage.value = ''

    try {
      await api.post('/auth/register', {
        email: email.value,
        password: password.value
      })

      router.push('/login')

    } catch (error) {
      errorMessage.value = 'Registration failed. Please try again.'
    } finally {
      loading.value = false
    }
  }
</script>

<style scoped>
  .register-card {
    border: 1px solid #ececec;
    box-shadow: 0 10px 40px rgba(0,0,0,0.08);
  }

  .register-background {
    min-height: 100vh;
    background:
      radial-gradient(circle at top left, #e0e7ff, transparent 30%),
      radial-gradient(circle at bottom right, #c7d2fe, transparent 30%),
      #f5f7fb;
  }

  .signin-link {
    color: #283593;
    text-decoration: none;
    font-weight: 500;
  }
  
  .cursor-pointer {
    cursor: pointer;
  }
</style>