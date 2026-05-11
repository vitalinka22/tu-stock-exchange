<template>

  <v-container max-width="40" >

    <v-card>

      <v-card-title>
        Register
      </v-card-title>

      <v-card-text>
        <v-form ref="form">

          <v-text-field 
            v-model="email"
            :rules="emailRules"
            label="Email"
            type="email"
          /> 

          <v-text-field
            v-model="password"
            :rules="passwordRules"
            label="Password"
            type="password"
          /> 

          <v-text-field
            v-model="username"
            :rules="usernameRules"
            label="Username"
            type="username"
          /> 

          <v-text-field
            v-model="confirmPassword"
            :rules="confirmPasswordRules"
            label="Confirm Password"
            type="password"
          /> 
  

          <v-alert v-if="errorMessage" type="error">
            {{ errorMessage }}
          </v-alert>

        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-btn @click="onSubmit" :loading="loading">
          Register
        </v-btn>


        <v-btn to="/login" variant="text">Already have an account? Login</v-btn>
      </v-card-actions>

    </v-card>
   
  </v-container>

</template>

<script setup lang="ts">
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'

  const email = ref('')
  const password = ref('')
  const loading = ref(false)
  const errorMessage = ref('')
  const form = ref<{ validate: () => Promise<{ valid: boolean }> } | null>(null)
  const username =ref('')
  const confirmPassword = ref('')

  const router = useRouter() 

  const emailRules = [
    (v: string) => !!v || 'Email is required',
    (v: string) => /.+@.+\..+/.test(v) || 'Email must be valid'
  ]

  const passwordRules = [
    (v: string) => !!v || 'Password is required',
    (v: string) => v.length >= 8 || 'Minimum 8 characters'
  ]

  const usernameRules = [
    (v: string) => !!v || 'Username is required',
    (v: string) => v.length >= 3 || 'Minimum 3 characters'
  ]

  const confirmPasswordRules = [
    (v: string) => !!v || 'Please confirm your password',
    (v: string) => v === password.value || 'Passwords do not match'
  ]

  async function onSubmit() {
    if (!form.value) return
    const { valid } = await form.value.validate()
    if (!valid ) return
    loading.value= true

    try {
   
      await new Promise(resolve => setTimeout(resolve, 1000))
      
      router.push('/login')
    
      } catch (error) {
        errorMessage.value = 'Invalid email or password'
      } finally {
        loading.value = false 
      }

    }

</script>