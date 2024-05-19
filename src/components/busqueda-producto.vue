<template>
    <div class="Menu-container">
      <div class="bar-blue-container">
        <h1>Buscar Por... </h1>
        <div class="closexA">
          <font-awesome-icon icon="fa-solid fa-times" class="close-icon"  @click="close"/>
        </div>
        <section class="titels table">
          <button class="search-option">Nombre</button>
          <button class="search-option">Producto</button>
          <button class="search-option">Marca</button>
          <button class="accept-button">Aceptar</button>
          <button class="cancel-button">Cancelar</button>
        </section>
        <section>
          <article class="fila1">
            <button class="decoration-f1"></button>
            <button class="decoration-f1"></button>
            <button class="decoration-f1"></button>
          </article>
          <article class="fila1">
            <button class="decoration-f1"></button>
            <button class="decoration-f1"></button>
            <button class="decoration-f1"></button>
          </article>
          <article class="fila1">
            <button class="decoration-f1"></button>
            <button class="decoration-f1"></button>
            <button class="decoration-f1"></button>
          </article>
          <article class="fila1">
            <button class="decoration-f1"></button>
            <button class="decoration-f1"></button>
            <button class="decoration-f1"></button>
          </article>
          <article class="fila1">
            <button class="decoration-f1"></button>
            <button class="decoration-f1"></button>
            <button class="decoration-f1"></button>
          </article>
        </section>
      </div>
    </div>
  </template>
  
  <script>3
  export default {
    name: 'Busqueda-producto'
     ,methods: {
    close() {
      this.$emit('close');
    }
  }
  }
  </script>
  
  <style scoped>
  .Menu-container{
    background: #ffff;
    width: 800px;
    height: 500px;
    border-radius: 20px;
  }
  .bar-blue-container{
    background: #004494;
    height: 50px;
    width: 800px; 
    margin-bottom: 20px;
    position: absolute;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
  }
  .closexA{
    color: white;
    font-size: 25px;
    cursor: pointer;
    padding: 12px;
    margin-left: 750px;
    margin-top: -65px;
  }
  h1{
    color: #ffff;
    font-size: 30px;
    margin-top: 10px;
    margin-left: 20px;
  }
  .titels {
    display: flex;
    gap: 10px;
    margin: 10px 0 20px 20px;
  }

  .search-option, .accept-button, .cancel-button {
    background-color: #004494;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 20px;
  }

  .accept-button {
    background-color: black;
  }

  .cancel-button {
    background-color: black;
  }
.fila1{
  display: flex;
  gap: 10px;
  margin: 30px 0 20px 20px;
}
.decoration-f1{
  background-color: #e3e8ff;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  width: 150px;
  height: 40px;
}
</style>
  