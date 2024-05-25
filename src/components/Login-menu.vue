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
    <div class="login-welcome">
      <h1>WELCOME</h1>
      <h2>Ventas</h2>
      <div class="button-welcome">
        <button @click="navigate('VentaProducto')">Estado de venta</button>
        <button @click="navigate('')">Análisis de Inventario</button>
      </div>
    </div>
    <img :src="require('@/assets/circular.png')" alt="Circular bar" class="caracteristicascir">
    <img :src="require('@/assets/barra.png')" alt="Circular bar" class="caracteristicascir2">
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
.caracteristicascir{
  width: 350px;
  height: 280px;
  margin-top: 100px;
  margin-left: -100px;
}
.caracteristicascir2{
  width: 300px;
  height: 250px;
  margin-left: -280PX;
  margin-top: 320px;
}
.Menu-container {
  background: #f4fbfe;
  width: 800px;
  height: 500px;
  border-radius: 20px;
  display: flex;
  flex-direction: row; /* Cambiado de column a row */
  padding: 20px;
  position: relative;
}

.Navegacion-color {
  background: #004494;
  height: 100%;
  width: 200px; 
  position: absolute;
  top: 0;
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
  margin-bottom: 20px;
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

.login-welcome {
  background: #f4fbfe;
  color: black;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start; /* Cambiado de center a flex-start */
  padding-left: 250px; /* Ajustar según sea necesario */
  justify-content: center;
}

h1 {
  font-size: 40px;
  color: black;
  margin-top: -200px;
  margin-left: 150px;
}

h2 {
  font-size: 45px;
  font-family: Arapey;
  color: black;
  margin-top: 10px;
  margin-bottom: 20px;
}

.button-welcome {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.button-welcome button {
  background: #004494;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 20px;
  cursor: pointer;
  font-size: 16px;
  text-align: center;
}

.button-welcome button:hover {
  background-color: #003366;
}
</style>
