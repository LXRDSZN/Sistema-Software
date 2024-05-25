<template>
  <div class="content-container">
    <div class="altas-color-blue">
      <div class="closexA">
        <font-awesome-icon icon="fa-solid fa-times" class="close-icon" @click="close"/>
      </div>
    </div>
    <h1>Alta de Producto</h1>
    <section class="Alta-Productos">
      <form class="container-decoration-form">
        <div class="form-group">
          <label for="Id_producto">Id_producto</label>
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
              <font-awesome-icon :icon="['fas', 'file-upload']"/>
            </div>
          </div>
        </div>
      </section>

      <div class="button-section">
        <button class="cancel-button" type="button">Cancelar</button>
        <button class="add-button" type="button" @click="showFirstModal">Agregar</button>
      </div>
    </section>

    <!-- Primera ventana modal -->
    <transition name="fade">
      <div class="modal" v-if="showModal1">
        <div class="modal-content1">
          <div class="bar-model1">
            <div class="modal-header1">
              <font-awesome-icon icon="fa-solid fa-times" class="close-icon" @click="closeFirstModal"/>
            </div>
          </div>
          
          <h2>¿Estás seguro de dar de alta El Producto?</h2>
          <div class="modal-buttons">
            <button class="modal-button" @click="showSecondModal">Continuar</button>
            <button class="modal-button" @click="closeFirstModal">Cancelar</button>
          </div>
        </div>
      </div>
    </transition>
 
    <!-- Segunda ventana modal -->
    <transition name="fade">
      <div class="modal" v-if="showModal2">
        <div class="modal-content2 success">
          <div class="bar-model1">
            <div class="modal-header2">
              <font-awesome-icon icon="fa-solid fa-times" class="close-icon" @click="closeSecondModal"/>
            </div>
          </div>
          <font-awesome-icon icon="fa-solid fa-check" class="check-icon"/>
          
          <h2>Producto agregado con éxito</h2>
          <p>Puedes visualizarlo en el apartado de búsqueda</p>
          <div class="modal-buttons">
            <button class="modal-button" @click="closeSecondModal">Aceptar</button>
          </div>
        </div>
      </div>
    </transition>
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
      selectedProduct: '',
      showModal1: false,
      showModal2: false
    }
  },
  methods: {
    close() {
      this.$emit('close');
    },
    showFirstModal() {
      this.showModal1 = true;
    },
    closeFirstModal() {
      this.showModal1 = false;
    },
    showSecondModal() {
      this.showModal1 = false;
      this.showModal2 = true;
    },
    closeSecondModal() {
      this.showModal2 = false;
    }
  }
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
}

.modal-content1 {
  background: white;
  border-radius: 20px;
  width: 500px;
  padding: 20px;
  font-family: 'Open Sans', sans-serif;
  position: relative;
}

.modal-content2 {
  background: white;
  border-radius: 20px;
  width: 500px;
  height: 320px;
  padding: 20px;
  font-family: 'Open Sans', sans-serif;
  position: relative;
}

.modal-header1 {
  display: flex;
  justify-content: flex-end;
  color: white;
  background: #004494;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  width: calc(100% + 20px);
  margin: -20px -20px 20px -20px;
  padding: 10px;
}

.modal-header2 {
  display: flex;
  justify-content: flex-end;
  color: white;
  background: #004494;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  width: calc(100% + 20px);
  margin: -20px -20px 20px -20px;
  padding: 10px;
}
.close-icon {
  cursor: pointer;
  font-size: 20px;
}

.modal-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
  gap: 20px;
}

.modal-buttons button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

.modal-buttons .modal-button {
  border-radius: 20px; /* Redondeado de los botones */
}

.modal-buttons button:first-child {
  background-color: #27CF04;
  color: white;
}

.modal-buttons button:last-child {
  background-color: black;
  color: white;
}

.success {
  background: #27CF04;
  color: white;
  border-radius: 20px;
  padding: 20px;
  width: 500px;
  text-align: center;
}

.success .modal-buttons {
  justify-content: center;
}

.check-icon {
  font-size: 50px;
  margin-bottom: 20px;
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
  margin-top: -250px;
  margin-left: 250px;
}

.upload-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  margin-top: -100px;
}

.upload-icon {
  font-size: 48px;
  color: red;
}

.button-section {
  display: flex;
  justify-content: space-between;
  width: 100px;
  margin-top: -150px;
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
  background-color: #27CF04;
  color: white;
}

.closexA {
  color: white;
  font-size: 25px;
  cursor: pointer;
  padding: 12px;
  margin-left: 590px;
}
</style>
