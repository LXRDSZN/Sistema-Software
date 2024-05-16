<template>
  <div>
    <MainIndex v-if="currentComponent === 'MainIndex'" @login-success="handleLoginSuccess" />
    <LoginMenu v-if="currentComponent === 'LoginMenu'" @navigate="handleNavigation" @logout="handleLogout" />
    <AltaProducto v-if="currentComponent === 'AltaProducto'" />
    <BajaProducto v-if="currentComponent === 'BajaProducto'" />
    <BusquedaProducto v-if="currentComponent === 'BusquedaProducto'" />
    <Soporte v-if="currentComponent === 'Soporte'" />
  </div>
</template>

<script>
import MainIndex from './components/MainIndex.vue'
import LoginMenu from './components/Login-menu.vue'
import AltaProducto from './components/Alta-producto.vue'
import BajaProducto from './components/Baja-producto.vue'
import BusquedaProducto from './components/busqueda-producto.vue'
import Soporte from './components/Soporte.vue'

export default {
  name: 'App',
  components: {
    MainIndex,
    LoginMenu,
    AltaProducto,
    BajaProducto,
    BusquedaProducto,
    Soporte
  },
  data() {
    return {
      currentComponent: 'MainIndex'
    }
  },
  methods: {
    handleLoginSuccess() {
      this.currentComponent = 'LoginMenu';
    },
    handleLogout() {
      this.currentComponent = 'MainIndex';
    },
    handleNavigation(component) {
      this.currentComponent = component;
    }
  }
}
</script>
