<template>
  <div class="Menu-container">
    <div class="Navegacion-color">
      <div class="menu-icon">
        <font-awesome-icon :icon="['fas', 'bars']" />
      </div>
      <nav class="menu-nav">
        <ul class="menu-list">
          <li @click="navigate('AltaProducto')">Altas</li>
          <li @click="navigate('BajaProducto')">Bajas</li>
          <li @click="navigate('BusquedaProducto')">Busquedas</li>
        </ul>
        <ul class="bottom-menu">
          <li @click="navigate('Soporte')">Soporte <font-awesome-icon :icon="['fas', 'headset']" /></li>
          <li @click="logout">Salir</li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginMenu',
  methods: {
    navigate(component) {
      this.$emit('navigate', component);
    },
    logout() {
      this.$emit('logout');
    }
  }
}
</script>

<style scoped>
.Menu-container {
  background: rgb(246, 246, 246);
  width: 800px;
  height: 500px;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start; 
  padding: 20px;
  position: relative;
}

.Navegacion-color {
  background: #004494;
  height: 100%;
  width: 200px; 
  position: absolute;
  top: 0px; 
  margin-left: -20px;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.menu-icon {
  padding: 10px;
  font-size: 24px;
  color: white;
  cursor: pointer;
}

.menu-nav {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

.menu-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.bottom-menu {
  list-style-type: none;
  padding: 0;
  margin-bottom: 20px; /* Ajusta según sea necesario */
}

li {
  color: white;
  padding: 10px 20px;
  cursor: pointer;
}

li:hover {
  background-color: #003366;
}

li i {
  margin-left: 10px;
}
</style>
