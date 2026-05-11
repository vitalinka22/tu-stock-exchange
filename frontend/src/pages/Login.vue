<template>

  <v-container max-width="40" >

    <v-card>

      <v-card-title>
        Login
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
  

          <v-alert v-if="errorMessage" type="error">
            {{ errorMessage }}
          </v-alert>

        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-btn @click="onSubmit" :loading="loading">
          Login
        </v-btn>


        <v-btn to="/register" variant="text">Don't have an account? Register</v-btn>
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
  const form = ref(null)

  const router = useRouter() 

  const emailRules = [
    (v: string) => !!v || 'Email is required',
    (v: string) => /.+@.+\..+/.test(v) || 'Email must be valid'
  ]

  const passwordRules = [
    (v: string) => !!v || 'Password is required',
    (v: string) => v.length >= 8 || 'Minimum 8 characters'
  ]

  async function onSumbit() {
    const { valid } = await form.value.validate()
    if (!value ) return
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