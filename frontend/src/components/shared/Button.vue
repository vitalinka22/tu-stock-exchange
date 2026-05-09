<template>
  <button 
    :type="type"
    :disabled="disabled"
    class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 disabled:opacity-50"
    @click="$emit('click')"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
defineProps<{
  type?: 'button' | 'submit'
  disabled?: boolean
}>()

defineEmits<{
  click: []
}>()
</script>