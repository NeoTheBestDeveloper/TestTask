// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css'

// Pinia
import { createPinia } from 'pinia'

// App
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App);
const pinia = createPinia();
const vuetify = createVuetify({
    components,
    directives,
});

app.use(router).use(pinia).use(vuetify).mount("#app");