<template>
  
  <div v-if = "type === 'spinner' ">
    <v-progress-circular
      :size = "spinnerSize"
      :color = "color"
    >
    </v-progress-circular>
  </div>

  <div v-else>
    <v-skeleton-loader
      :type = "type"
    >
    </v-skeleton-loader>
  </div>
  
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  size: 'small' | 'medium' | 'large'
  type: 'spinner' | 'skeleton' 
  color?: 'primary' | 'success' | 'error' | 'warning' 
}>(), {
  size: 'medium',
  type: 'spinner',
  color: 'primary',
})

const sizeMap = { small:24, medium:48, large: 64}
const spinnerSize = computed (() => sizeMap[props.size])

</script>