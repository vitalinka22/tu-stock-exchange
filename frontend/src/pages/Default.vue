
<template>
    
    <v-container style="min-height: 100vh; background-color: #000" class="d-flex align-center justify-center" >

        <v-card width="420" class="pa-8" elevation="0" rounded="xl">

            <v-icon size ="80" color="red">mdi-alert-circle</v-icon>

            <v-card-title class="text-h5 font-weight-bold pb-1">
                You've gone bankrupt
            </v-card-title>

            <v-card-text>
                Your portfolio value has fallen too low to continue trading.
                You can start over with $1000.
            </v-card-text>

            <v-card-actions>

                <v-btn
                block
                size="large"
                color="red"
                @click = "showModal = true"
                variant="flat"
                class="mt-4 text-none font-weight-bold"
                rounded="lg"
                >
                Start Over
                </v-btn>
            </v-card-actions>

            <Modal 
            v-model = "showModal" 
            title="Are you sure?"
            confirmationText="You will restart with $1000. All your holdings will be liquidated."
            @confirm="onStartOver"
            @cancel="showModal = false"
            />

      </v-card>
     
    </v-container>

</template>

<script setup lang="ts">

    import { useRouter } from 'vue-router'
    
    import { ref } from 'vue'
    import Modal from '../components/shared/Modal.vue'


    const router = useRouter()

    function onStartOver () {
        // user gets redirected to market page
        // later needs to be bound to backend
        router.push('/market')
    }

    const showModal = ref(false)


</script>

