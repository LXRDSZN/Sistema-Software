<template>
  <div class="Menu-container">
    <div class="Navegacion-color">
      <nav>
        <ul>
          <li @click="navigate('AltaProducto')">Alta Producto</li>
          <li @click="navigate('BajaProducto')">Baja Producto</li>
          <li @click="navigate('BusquedaProducto')">Búsqueda</li>
          <li @click="navigate('Soporte')">Soporte</li>
          <li @click="logout">Salir</li>
        </ul>
      </nav>
    </div>
    <div class="">
      <!-- Aquí puedes agregar contenido adicional si es necesario -->
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
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  color: white;
  padding: 10px;
  cursor: pointer;
}
li:hover {
  background-color: #003366;
}
</style>
