<template>
  <div class="content-container">
    <div class="altas-color-blue">
      <div class="closexA">
        <font-awesome-icon icon="fa-solid fa-times" class="close-icon"  @click="close"/>
      </div>
    </div>
    <h1>Alta de Producto</h1>
    <section class="Alta-Productos">
      <form class="container-decoration-form">
        <div class="form-group">
          <label for="Id_producto">Id_producto </label>
          <input type="text" id="Id_producto" v-model="Id_producto" required placeholder="Producto">
        </div>
        <div class="form-group">
          <label for="Nom_producto">Producto</label>
          <input type="text" id="Nom_producto" v-model="Nom_producto" required placeholder="Producto">
        </div>
        <div class="form-group">
          <label for="Cantidad_producto">Cantidad</label>
          <input type="text" id="Cantidad_producto" v-model="Cantidad_producto" required placeholder="Cantidad">
        </div>
        <div class="form-group">
          <label for="Precio_producto">Precio</label>
          <input type="text" id="Precio_producto" v-model="Precio_producto" required placeholder="Precio">
        </div>
        <button class="modify-button" type="button">Modificar</button>
      </form>

      <section class="subir-producto">
        <div class="upload-section">
        <label for="product-select">Producto</label>
        <select id="product-select" v-model="selectedProduct">
          <option value="" disabled>Seleccionar producto</option>
          <!-- Opciones de productos -->
        </select>
        <div class="upload-container">
          <p>Subir Datos</p>
          <div class="upload-icon">
            <font-awesome-icon :icon="['fas', 'file-upload']" />
          </div>
        </div>
      </div>
      </section>
     
      <div class="button-section">
        <button class="cancel-button" type="button">Cancelar</button>
        <button class="add-button" type="button">Agregar</button>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'AltaProducto',
  data() {
    return {
      Id_producto: '',
      Nom_producto: '',
      Cantidad_producto: '',
      Precio_producto: '',
      selectedProduct: ''
    }
  }
  ,
  methods: {
    close() {
      this.$emit('close');
    }
  }
}
</script>

<style scoped>

.subir-producto{
  background: #f4fbfe;
  margin-top: -250px;
  margin-left: 220px;
}
.content-container {
  background: rgb(255, 255, 255);
  width: 600px;
  height: 500px;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start; 
  align-items: center;
  padding: 20px;
  font-family: 'Open Sans', sans-serif;
  position: relative;
}

.altas-color-blue {
  background: #004494;
  height: 50px;
  width: 100%;
  margin-bottom: 20px;
  position: absolute;
  top: 0;
  left: 0;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
}

h1 {
  margin-top: 60px; /* Ajustar para que el título se vea bien */
}

.Alta-Productos {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.container-decoration-form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-left: -350px;
}

.form-group {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 15px;
}

.form-group label {
  width: 80px; /* Ajustar el ancho de la etiqueta */
  margin-right: 10px;
}

.form-group input {
  flex: 1;
  border: none;
  border-bottom: 2px solid #ccc;
  padding: 10px 0;
  background: transparent;
  outline: none;
}

.form-group input:focus {
  border-bottom: 2px solid #87CEEB;
}

.modify-button {
  background-color: orange;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
  align-self: center;
  margin-top: 50px;
}

.upload-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.upload-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  margin-top: 10px;
}

.upload-icon {
  font-size: 48px;
  color: red;
}

.button-section {
  display: flex;
  justify-content: space-between;
  width: 100px;
  margin-top: 20px;
  margin-left: 100px;
}

.cancel-button, .add-button {
  flex: 1;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin: 0 10px;
}

.cancel-button {
  background-color: black;
  color: white;
}

.add-button {
  background-color: green;
  color: white;
  
}
.closexA{
  color: white;
  font-size: 25px;
  cursor: pointer;
  padding: 12px;
  margin-left: 590px;
}
</style>