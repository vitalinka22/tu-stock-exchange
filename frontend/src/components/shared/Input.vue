<template>
  
  <v-text-field
    :model-value = "modelValue"
    @update:model-value="emit('update:modelValue', Number($event))"    :label = "label"
    :placeholder = "placeholder"
    :prefix = "prefix"
    :type = "type"
    :disabled = "disabled"
    :error = "hasError"
    :error-messages = "errorMessage"
  >
    
  </v-text-field>
  
  
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  label: string
  modelValue: number
  placeholder: string
  type: 'text' | 'number'
  disabled: boolean
  error: boolean
  errorMessage: string  
  prefix?: string
}>(), {
  type: 'text',
  disabled: false,
  error: false,
})

const emit = defineEmits<{
  'update:modelValue': [value: number]
}>()

const hasError = computed(() => props.error && !!props.errorMessage)

</script>