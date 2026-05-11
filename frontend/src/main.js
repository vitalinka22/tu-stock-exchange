import './assets/style.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router/index.js' //router
import App from './App.vue'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'

const vuetify = createVuetify()  

const app = createApp(App)

app.use(router)
app.use(createPinia())
app.use(vuetify)  
app.mount('#app')