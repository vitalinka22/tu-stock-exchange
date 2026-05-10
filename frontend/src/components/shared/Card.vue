<template>
  <v-card>
    <v-skeleton-loader v-if="loading" type="card" />

    <template v-else>

      <v-card-item>
        <v-card-title>{{ ticker }}</v-card-title>
        <v-card-subtitle>{{ companyName }}</v-card-subtitle>
      </v-card-item>

      <v-card-text>
        <p> {{ formattedPrice }}</p>
        <span :class="changeColor">{{ formattedChange }} ({{ formattedPercent }})</span>
      </v-card-text>

      <div style="height: 60px; background: lightgrey;" />

      <v-card-actions>
        <v-btn color="success" @click="emit('buy', props.ticker)">Buy</v-btn>
        <v-btn color="error" variant="outlined" @click="emit('sell', props.ticker)">Sell</v-btn>
      </v-card-actions>

    </template>

  </v-card>
  
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  ticker: string
  companyName: string
  price: number
  change: number
  changePercent: number
  currency: string
  loading: boolean  
}>(), {
  currency: 'USD',
  loading: false
})

const emit = defineEmits<{
  buy: [ticker: string]
  sell: [ticker: string]
}>()

const isPositive = computed(() => props.change >= 0)

const formattedPrice = computed (() => props.price.toLocaleString())

const formattedChange = computed (() => props.change.toLocaleString())

const formattedPercent = computed (() => {
  const sign = isPositive.value ? '+' : ''
  return `${sign}${props.changePercent.toFixed(2)}%`
})

const changeColor = computed (() =>  isPositive.value ? 'text-success' : 'text-error')

</script>