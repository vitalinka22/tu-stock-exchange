<template>
  
<v-dialog :model-value="modelValue" :persistent="!closeOnOverlay">
  <v-card>
    <v-card-title>{{ title }}</v-card-title>
    <v-card-text>{{ confirmationText }}</v-card-text>
    <v-card-actions>
      <v-btn @click="emit('cancel'); emit('update:modelValue', false)">Cancel</v-btn>
      <v-btn color="success" @click="emit('confirm'); emit('update:modelValue', false)">Confirm</v-btn>
    </v-card-actions>
  </v-card>
</v-dialog>
  
</template>

<script setup lang="ts">

const props = withDefaults(defineProps<{
  title: string
  modelValue: boolean
  confirmationText: string
  closeOnOverlay?: boolean
}>(), {
  closeOnOverlay: true,
})

const emit = defineEmits<{
  confirm: []
  cancel: []
  'update:modelValue' : [value: boolean]
}>()


</script>