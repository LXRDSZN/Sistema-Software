<template>
  <div class="Login-main">
    <div class="Login-bar-blue"></div>
    <div class="login-content">
      <form class="login-form">
        <div class="input-icon-container">
          <input type="text" id="username" name="username" required placeholder="Usuario">
          <font-awesome-icon icon="user" class="input-icon"/>
        </div>
        <div class="input-icon-containerpass">
          <input type="password" id="password" name="password" required placeholder="Contraseña">
          <font-awesome-icon icon="lock" class="input-icon-pass" />
        </div>
        <button type="submit">Iniciar Sesión</button>
      </form>
      <div class="logo-rh">
        <img src="/src/assets/rh.jpg">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MainIndex',
  props: {
    msg: String
  }
}
</script>

<style>
/* Estilos para el input de contraseña */
.input-icon-containerpass {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon-containerpass input {
  flex-grow: 1;
  padding-right: 30px; 
}

.input-icon-containerpass .input-icon-pass {
  position: absolute;
  right: 10px; 
  color: #060505;
}

/* Estilos para el input de usuario */
.input-icon-container {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon-container input {
  flex-grow: 1;
  padding-right: 30px; 
}

.input-icon-container .input-icon {
  position: absolute;
  right: 10px; 
  color: #060505;
}

/* Estilos globales */
body {
  background: #8C52FF;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; 
  margin: 0; 
}

.Login-main {
  background: rgb(246, 246, 246);
  width: 800px;
  height: 500px;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start; 
  padding: 20px;
  position: relative;
}

.Login-bar-blue {
  background: #004494;
  height: 50px;
  width: 840px; 
  margin-bottom: 20px;
  position: absolute;
  top: 0px; 
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
}

.login-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 650px;
  margin-top: 25%; 
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 50%; 
}

.login-form input {
  border: none;
  border-bottom: 2px solid #ccc;
  padding: 10px 0;
  background: transparent;
  outline: none;
}

.login-form input:focus {
  border-bottom: 2px solid #87CEEB; /* Color del borde al enfocar */
}

button {
  padding: 10px;
  background-color: #0056b3;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: 100%;
}

button:hover {
  background-color: #004494;
}

.logo-rh img {
  width: 100%; 
  max-width: 150px; 
  margin-left: 20px; 
}
</style>
