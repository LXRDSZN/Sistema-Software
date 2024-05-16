<template>
  <div>
    <MainIndex v-if="currentComponent === 'MainIndex'" @login-success="handleLoginSuccess" />
    <div v-else>
      <LoginMenu @navigate="handleNavigation" @logout="handleLogout" />
      <component :is="currentComponent" v-if="currentComponent !== 'MainIndex' && currentComponent !== 'LoginMenu'"></component>
    </div>
  </div>
</template>

<script>
import MainIndex from './components/MainIndex.vue'
import LoginMenu from './components/Login-menu.vue'
import AltaProducto from './components/Alta-producto.vue'
import BajaProducto from './components/Baja-producto.vue'
import BusquedaProducto from './components/busqueda-producto.vue'
import SoporteVue from './components/Soporte.vue'
export default {
  name: 'App',
  components: {
    MainIndex,
    LoginMenu,
    AltaProducto,
    BajaProducto,
    BusquedaProducto,
    SoporteVue
  },
  data() {
    return {
      currentComponent: 'MainIndex'
    }
  },
  methods: {
    handleLoginSuccess() {
      this.currentComponent = 'AltaProducto';  // Cambia esto al componente que deseas mostrar por defecto después del login
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
