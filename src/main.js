import { createApp } from 'vue';
import App from './App.vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faUser, faLock } from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';

// Agrega los iconos que desees utilizar
library.add(faUser);
library.add(faLock);

// Crear la aplicación
const app = createApp(App);

// Configurar la URL base para Axios
axios.defaults.baseURL = 'http://localhost:5000';  // Asegúrate de que esta URL apunte a tu backend

// Registra FontAwesomeIcon globalmente
app.component('font-awesome-icon', FontAwesomeIcon);

// Montar la aplicación
app.mount('#app');
