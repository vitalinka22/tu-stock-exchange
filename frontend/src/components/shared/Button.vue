<template>
  <v-btn
  :label="label"
  :variant="buttonVariant"
  :disabled="disabled || loading"
  :loading="loading"
  @click="emit('click')"
  :color="buttonColor"
>
 {{ label }}
</v-btn>
</template>

<script setup lang="ts">
import { computed } from 'vue'

// props
const props = withDefaults(defineProps<{
  label: string
  variant: 'primary' | 'destructive' | 'ghost'
  disabled: boolean
  loading: boolean
}>(), { // standard wert
  variant: 'primary',
  disabled: false,
  loading: false
})

const emit = defineEmits<{
  click: []
}>()

const buttonVariant = computed(() => {
  const variants = {
    primary: 'flat',
    destructive: 'flat',
    ghost: 'outlined'
  } as const
  return variants[props.variant]
})

const buttonColor = computed(() => {
  const colors = {
    primary: 'primary',
    destructive: 'error',
    ghost: undefined
  }
  return colors[props.variant]
})
  
</script>