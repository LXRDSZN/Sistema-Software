<template>
    <div class="Menu-container">
      <div class="Navegacion-color">

      </div>
        <div class="icon-title">
          <font-awesome-icon icon="fa-solid fa-times" class="close-icon" @click="close"/>
          <h1>Ventas</h1>
        </div>
        <div class="container-buttons">
          <div class="container-cuestions">
            <form class="container-decoration-form">
              <div class="form-group">
                <label for="Id_producto">Id_Producto.</label>
                <input type="text" id="Id_producto" v-model="Id_producto" required placeholder="Producto">
              </div>
              <div class="form-group">
                <label for="Nom_producto">Nombre</label>
                <input type="text" id="Nom_producto" v-model="Nom_producto" required placeholder="Nombre">
              </div>
              <div class="form-group">
                <label for="Cantidad_producto">Fecha</label>
                <input type="text" id="Cantidad_producto" v-model="Cantidad_producto" required placeholder="Fecha de Venta">
              </div>
              <div class="form-group">
                <label for="Precio_producto">Monto</label>
                <input type="text" id="Precio_producto" v-model="Precio_producto" required placeholder="Precio">
              </div>
            </form>
            <div class="modal-buttons">
              <button class="modal-button" @click="showSecondModal">Pagar</button>
              <button class="modal-button" @click="closeFirstModal">Cancelar</button>
            </div>
          </div>
        </div>      
    </div>
  </template>
  
  <script>
  export default {
    name: 'VentaProducto',
    methods: {
      navigate(component) {
        this.$emit('navigate', component);
      },
      logout() {
        this.$emit('logout');
      },
      close() {
      this.$emit('close');
    }
    }
  }
  </script>
  
  <style scoped>
  .Menu-container {
    background: #ffffff;
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

  .icon-title{
    background: white;
    width: 620px;
    height: 50px;
    margin-left:200px;
    border-top-right-radius: 20px;
    margin-top:-20px ;
  }
  h1{
    color: black;
    font-size: 35px;
    margin-left:260px;
  }

  .close-icon {
    color: black;
    cursor: pointer;
    font-size: 25px;
    margin-top: 10px;
    margin-left:95% ;
  }
  .container-cuestions{
    background: white;
    width: 520px;
    height: 300px;
    margin-top:100px;
    margin-left: 100px;
  }
  .container-buttons{
    background: white;
    width:100%x;
    height: 350px;
    margin-top:80px;
    margin-left: -700px;
  }
  .container-decoration-form {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-left:0px;
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
  .modal-buttons {
    display: flex;
    justify-content: space-between;
    margin-top: 60px;
    gap: 250px;
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
    background-color: #40B8F5;
    color: white;
  }

  .modal-buttons button:last-child {
    background-color: black;
    color: white;
  }

</style>
  