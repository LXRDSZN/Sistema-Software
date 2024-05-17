<template>
  <div>
    <MainIndex v-if="currentComponent === 'MainIndex'" @login-success="handleLoginSuccess" />
    <LoginMenu v-if="currentComponent === 'LoginMenu'" @navigate="handleNavigation" @logout="handleLogout" />
    <AltaProducto v-if="currentComponent === 'AltaProducto'" @close="handleClose" />
    <BajaProducto v-if="currentComponent === 'BajaProducto'" @close="handleClose" />
    <BusquedaProducto v-if="currentComponent === 'BusquedaProducto'" @close="handleClose" />
    <Soporte v-if="currentComponent === 'Soporte'" @close="handleClose" />
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
    },
    handleClose() {
      this.currentComponent = 'LoginMenu';
    }
  }
}
</script>
